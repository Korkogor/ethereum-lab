from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv
import os

# Загружаем переменные из .env
load_dotenv()

# 1. Подключение к локальному Anvil
rpc_url = os.getenv("RPC_URL")
w3 = Web3(Web3.HTTPProvider(rpc_url))

if w3.is_connected():
    print(f"✅ Подключено к Anvil. Блок: {w3.eth.block_number}, Chain ID: {w3.eth.chain_id}")
else:
    print("❌ Ошибка подключения. Проверьте, запущен ли Anvil.")
    exit()

# Получаем аккаунт из приватного ключа
private_key = os.getenv("PRIVATE_KEY")
acct = Account.from_key(private_key)
print(f"Наш адрес (отправитель): {acct.address}")
balance_wei = w3.eth.get_balance(acct.address)
print(f"Наш баланс: {w3.from_wei(balance_wei, 'ether')} ETH")

def send_tx(to_address, amount_eth):
    # Получаем баланс получателя ДО транзакции
    balance_before_wei = w3.eth.get_balance(to_address)
    balance_before_eth = w3.from_wei(balance_before_wei, 'ether')

    print(f"\n--- НАЧАЛО ТРАНЗАКЦИИ ---")
    print(f"Отправляем {amount_eth} ETH")
    print(f"От: {acct.address}")
    print(f"Кому: {to_address}")
    print(f"Баланс получателя ДО: {balance_before_eth} ETH")

    nonce = w3.eth.get_transaction_count(acct.address)

    tx = {
        'nonce': nonce,
        'to': to_address,
        'value': w3.to_wei(amount_eth, 'ether'),
        'gas': 21000,
        'gasPrice': w3.eth.gas_price,
        'chainId': int(os.getenv("CHAIN_ID"))
    }

    # Подпись и отправка
    signed = acct.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)

    print("Ожидание подтверждения...")
    # Ожидание чека
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    print(f"✅ Транзакция успешна!")
    print(f"Хэш: {tx_hash.hex()}")
    print(f"Статус: {'Успех' if receipt.status == 1 else 'Ошибка'}")

    # Получаем баланс получателя ПОСЛЕ транзакции
    balance_after_wei = w3.eth.get_balance(to_address)
    balance_after_eth = w3.from_wei(balance_after_wei, 'ether')
    print(f"Баланс получателя ПОСЛЕ: {balance_after_eth} ETH")
    print(f"--- КОНЕЦ ТРАНЗАКЦИИ ---\n")

# Адрес получателя (Account #1 из Anvil)
to_address = "0x70997970C51812dc3A010C7d01b50e0d17dc79C8"
# Отправляем 0.5 ETH
send_tx(to_address, 0.5)
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv
import os

# Загружаем переменные из .env
load_dotenv()

# 1. Подключение к локальному Anvil
rpc_url = os.getenv("RPC_URL")
w3 = Web3(Web3.HTTPProvider(rpc_url))

if w3.is_connected():
    print(f"✅ Подключено к Anvil. Блок: {w3.eth.block_number}, Chain ID: {w3.eth.chain_id}")
else:
    print("❌ Ошибка подключения. Проверьте, запущен ли Anvil.")
    exit()

# Получаем аккаунт из приватного ключа
private_key = os.getenv("PRIVATE_KEY")
acct = Account.from_key(private_key)
print(f"Наш адрес (отправитель): {acct.address}")
balance_wei = w3.eth.get_balance(acct.address)
print(f"Наш баланс: {w3.from_wei(balance_wei, 'ether')} ETH")

def send_tx(to_address, amount_eth):
    # Получаем баланс получателя ДО транзакции
    balance_before_wei = w3.eth.get_balance(to_address)
    balance_before_eth = w3.from_wei(balance_before_wei, 'ether')

    print(f"\n--- НАЧАЛО ТРАНЗАКЦИИ ---")
    print(f"Отправляем {amount_eth} ETH")
    print(f"От: {acct.address}")
    print(f"Кому: {to_address}")
    print(f"Баланс получателя ДО: {balance_before_eth} ETH")

    nonce = w3.eth.get_transaction_count(acct.address)

    tx = {
        'nonce': nonce,
        'to': to_address,
        'value': w3.to_wei(amount_eth, 'ether'),
        'gas': 21000,
        'gasPrice': w3.eth.gas_price,
        'chainId': int(os.getenv("CHAIN_ID"))
    }

    # Подпись и отправка
    signed = acct.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)

    print("Ожидание подтверждения...")
    # Ожидание чека
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    print(f"✅ Транзакция успешна!")
    print(f"Хэш: {tx_hash.hex()}")
    print(f"Статус: {'Успех' if receipt.status == 1 else 'Ошибка'}")

    # Получаем баланс получателя ПОСЛЕ транзакции
    balance_after_wei = w3.eth.get_balance(to_address)
    balance_after_eth = w3.from_wei(balance_after_wei, 'ether')
    print(f"Баланс получателя ПОСЛЕ: {balance_after_eth} ETH")
    print(f"--- КОНЕЦ ТРАНЗАКЦИИ ---\n")

# Адрес получателя (Account #1 из Anvil)
to_address = "0x70997970C51812dc3A010C7d01b50e0d17dc79C8"
# Отправляем 0.5 ETH
send_tx(to_address, 0.5)
