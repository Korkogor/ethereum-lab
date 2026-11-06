import json
from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv("RPC_URL")))
contract_address = os.getenv("CONTRACT_ADDRESS")

with open("artifacts/HelloWorld.json") as f:
    contract_json = json.load(f)

contract = w3.eth.contract(address=contract_address, abi=contract_json["abi"])
message = contract.functions.getMessage().call()

print(f"Сообщение из контракта: {message}")
