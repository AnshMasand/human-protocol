import json

from web3 import Web3
from web3.middleware import construct_sign_and_send_raw_middleware
from web3.providers.rpc import HTTPProvider

from eth_account.messages import encode_defunct

from src.core.constants import Networks
from src.core.config import Config


def get_web3(chain_id: Networks):
    match chain_id:
        case Config.polygon_mainnet.chain_id:
            w3 = Web3(HTTPProvider(Config.polygon_mainnet.rpc_api))
            gas_payer = w3.eth.account.from_key(Config.polygon_mainnet.private_key)
            w3.middleware_onion.add(
                construct_sign_and_send_raw_middleware(gas_payer),
                "construct_sign_and_send_raw_middleware",
            )
            w3.eth.default_account = gas_payer.address
            return w3
        case Config.polygon_mumbai.chain_id:
            w3 = Web3(HTTPProvider(Config.polygon_mumbai.rpc_api))
            gas_payer = w3.eth.account.from_key(Config.polygon_mumbai.private_key)
            w3.middleware_onion.add(
                construct_sign_and_send_raw_middleware(gas_payer),
                "construct_sign_and_send_raw_middleware",
            )
            w3.eth.default_account = gas_payer.address
            return w3
        case Config.localhost.chain_id:
            w3 = Web3(HTTPProvider(Config.localhost.rpc_api))
            gas_payer = w3.eth.account.from_key(Config.localhost.private_key)
            w3.middleware_onion.add(
                construct_sign_and_send_raw_middleware(gas_payer),
                "construct_sign_and_send_raw_middleware",
            )
            w3.eth.default_account = gas_payer.address
            return w3
        case _:
            raise ValueError(f"{chain_id} is not in available list of networks.")


def sign_message(chain_id: Networks, message) -> str:
    w3 = get_web3(chain_id)
    private_key = ""
    match chain_id:
        case Config.polygon_mainnet.chain_id:
            private_key = Config.polygon_mainnet.private_key
        case Config.polygon_mumbai.chain_id:
            private_key = Config.polygon_mumbai.private_key
        case Config.localhost.chain_id:
            private_key = Config.localhost.private_key
        case _:
            raise ValueError(f"{chain_id} is not in available list of networks.")

    signed_message = w3.eth.account.sign_message(
        encode_defunct(text=json.dumps(message, separators=(",", ":"))), private_key
    )

    return signed_message.signature.hex()


def recover_signer(chain_id: Networks, message, signature: str) -> str:
    w3 = get_web3(chain_id)
    message_hash = encode_defunct(text=json.dumps(message, separators=(",", ":")))
    signer = w3.eth.account.recover_message(message_hash, signature=signature)

    return signer


def validate_address(escrow_address: str) -> str:
    if not Web3.isAddress(escrow_address):
        raise ValueError(f"{escrow_address} is not a correct Web3 address")
    return Web3.toChecksumAddress(escrow_address)
