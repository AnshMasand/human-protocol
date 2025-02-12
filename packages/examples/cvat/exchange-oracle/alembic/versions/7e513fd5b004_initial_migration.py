"""Initial migration

Revision ID: 7e513fd5b004
Revises: 
Create Date: 2023-07-20 17:44:57.028850

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = "7e513fd5b004"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "projects",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("cvat_id", sa.Integer(), nullable=False),
        sa.Column("cvat_cloudstorage_id", sa.Integer(), nullable=False),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column("job_type", sa.String(), nullable=False),
        sa.Column("escrow_address", sa.String(length=42), nullable=False),
        sa.Column("chain_id", sa.Integer(), nullable=False),
        sa.Column("bucket_url", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("bucket_url"),
        sa.UniqueConstraint("escrow_address"),
    )
    op.create_index(
        op.f("ix_projects_cvat_cloudstorage_id"),
        "projects",
        ["cvat_cloudstorage_id"],
        unique=False,
    )
    op.create_index(op.f("ix_projects_cvat_id"), "projects", ["cvat_id"], unique=True)
    op.create_index(op.f("ix_projects_id"), "projects", ["id"], unique=False)
    op.create_table(
        "webhooks",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("signature", sa.String(), nullable=False),
        sa.Column("escrow_address", sa.String(length=42), nullable=False),
        sa.Column("chain_id", sa.Integer(), nullable=False),
        sa.Column("s3_url", sa.String(), nullable=True),
        sa.Column("type", sa.String(), nullable=False),
        sa.Column("status", sa.String(), server_default="pending", nullable=True),
        sa.Column("attempts", sa.Integer(), server_default="0", nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "wait_until",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("escrow_address", "type", name="_escrow_address_type_uc"),
    )
    op.create_index(op.f("ix_webhooks_id"), "webhooks", ["id"], unique=False)
    op.create_index(
        op.f("ix_webhooks_signature"), "webhooks", ["signature"], unique=True
    )
    op.create_table(
        "tasks",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("cvat_id", sa.Integer(), nullable=False),
        sa.Column("cvat_project_id", sa.Integer(), nullable=False),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["cvat_project_id"], ["projects.cvat_id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_tasks_cvat_id"), "tasks", ["cvat_id"], unique=True)
    op.create_index(op.f("ix_tasks_id"), "tasks", ["id"], unique=False)
    op.create_table(
        "jobs",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("cvat_id", sa.Integer(), nullable=False),
        sa.Column("cvat_task_id", sa.Integer(), nullable=False),
        sa.Column("cvat_project_id", sa.Integer(), nullable=False),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column("assignee", sa.String(length=42), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["cvat_project_id"], ["projects.cvat_id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["cvat_task_id"], ["tasks.cvat_id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_jobs_assignee"), "jobs", ["assignee"], unique=False)
    op.create_index(op.f("ix_jobs_cvat_id"), "jobs", ["cvat_id"], unique=True)
    op.create_index(op.f("ix_jobs_id"), "jobs", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_jobs_id"), table_name="jobs")
    op.drop_index(op.f("ix_jobs_cvat_id"), table_name="jobs")
    op.drop_index(op.f("ix_jobs_assignee"), table_name="jobs")
    op.drop_table("jobs")
    op.drop_index(op.f("ix_tasks_id"), table_name="tasks")
    op.drop_index(op.f("ix_tasks_cvat_id"), table_name="tasks")
    op.drop_table("tasks")
    op.drop_index(op.f("ix_webhooks_signature"), table_name="webhooks")
    op.drop_index(op.f("ix_webhooks_id"), table_name="webhooks")
    op.drop_table("webhooks")
    op.drop_index(op.f("ix_projects_id"), table_name="projects")
    op.drop_index(op.f("ix_projects_cvat_id"), table_name="projects")
    op.drop_index(op.f("ix_projects_cvat_cloudstorage_id"), table_name="projects")
    op.drop_table("projects")
    # ### end Alembic commands ###
