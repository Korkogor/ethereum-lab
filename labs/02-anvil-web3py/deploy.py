import json
from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv("RPC_URL")))
private_key = os.getenv("PRIVATE_KEY")
account = w3.eth.account.from_key(private_key)

# Загрузка ABI и bytecode
with open("artifacts/HelloWorld.json") as f:
    contract_json = json.load(f)

abi = contract_json["abi"]
bytecode = contract_json["data"]["bytecode"]["object"]

# Создание контракта
HelloWorld = w3.eth.contract(abi=abi, bytecode=bytecode)

# Построение транзакции
tx = HelloWorld.constructor().build_transaction({
    "from": account.address,
    "nonce": w3.eth.get_transaction_count(account.address),
    "gas": 3000000,
    "gasPrice": w3.eth.gas_price,
})

# Подпись и отправка
signed = account.sign_transaction(tx)
tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Контракт развёрнут: {receipt.contractAddress}")
