from eth_account.signers.base import BaseAccount
from web3 import Web3
from eth_typing import HexStr
from web3.types import TxReceipt
from tests.contracts.utils import get_abi, get_hex_binary


class CounterContract:

    def __init__(self, web3: Web3, address: HexStr, abi=None):
        self.web3 = web3
        if abi is None:
            abi = get_abi("counter_contract_abi.json")
        self.contract = self.web3.zksync.contract(address=address, abi=abi)

    def get(self):
        return self.contract.functions.get().call()

    def increment(self, v: int) -> TxReceipt:
        tx_hash = self.contract.functions.increment(v).transact()
        tx_receipt = self.web3.zksync.wait_for_transaction_receipt(tx_hash)
        return tx_receipt

    @classmethod
    def deploy(cls, web3: Web3, account: BaseAccount) -> 'CounterContract':
        abi = get_abi("counter_contract_abi.json")
        counter_contract_instance = web3.zksync.contract(abi=abi,
                                                         bytecode=get_hex_binary("counter_contract.hex"))
        tx_hash = counter_contract_instance.constructor().transact(
            {
                "from": account.address,
            }
        )
        tx_receipt = web3.zksync.wait_for_transaction_receipt(tx_hash)
        return cls(web3, tx_receipt["contractAddress"], abi)

    @property
    def address(self):
        return self.contract.address


class CounterContractEncoder:
    def __init__(self, web3: Web3):
        self.web3 = web3
        self.counter_contract = self.web3.eth.contract(abi=get_abi("counter_contract_abi.json"),
                                                       bytecode=get_hex_binary("counter_contract.hex"))

    def encode_method(self, fn_name, args: list) -> HexStr:
        return self.counter_contract.encodeABI(fn_name, args)
