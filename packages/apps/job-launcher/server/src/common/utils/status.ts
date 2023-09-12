import { JobStatus, JobStatusFilter } from '../enums/job';

export function filterToDatabaseStatus(
  filterStatus: JobStatusFilter,
): JobStatus[] {
  switch (filterStatus) {
    case JobStatusFilter.PENDING:
      return [JobStatus.PENDING, JobStatus.PAID];
    case JobStatusFilter.LAUNCHED:
      return [JobStatus.LAUNCHED];
    case JobStatusFilter.COMPLETED:
      return [JobStatus.COMPLETED];
    case JobStatusFilter.CANCELED:
      return [JobStatus.CANCELED, JobStatus.TO_CANCEL];
    case JobStatusFilter.FAILED:
      return [JobStatus.FAILED];
  }
}

export function databaseToFilterStatus(status: JobStatus): JobStatusFilter {
  switch (status) {
    case JobStatus.PENDING:
    case JobStatus.PAID:
      return JobStatusFilter.PENDING;
    case JobStatus.LAUNCHED:
      return JobStatusFilter.LAUNCHED;
    case JobStatus.COMPLETED:
      return JobStatusFilter.COMPLETED;
    case JobStatus.CANCELED:
    case JobStatus.TO_CANCEL:
      return JobStatusFilter.CANCELED;
    case JobStatus.FAILED:
      return JobStatusFilter.FAILED;
  }
}
