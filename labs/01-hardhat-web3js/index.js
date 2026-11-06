import { Web3 } from 'web3';

// 1. Подключаемся к локальному узлу Hardhat
const rpcUrl = 'http://127.0.0.1:8545'; 
const web3 = new Web3(new Web3.providers.HttpProvider(rpcUrl));

// 2. Вставляем приватный ключ аккаунта #0 из терминала Hardhat
const privateKey = '0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80'; // ПРИМЕР! Замените на свой
const account = web3.eth.accounts.privateKeyToAccount(privateKey);
web3.eth.accounts.wallet.add(account);

async function run() {
    try {
        // Проверка подключения
        const blockNumber = await web3.eth.getBlockNumber();
        const chainId = await web3.eth.getChainId();
        console.log(`✅ Подключено к Hardhat. Блок: ${blockNumber}, Chain ID: ${chainId} (должен быть 31337)`);

        // Чтение баланса
        const balanceWei = await web3.eth.getBalance(account.address);
        console.log(`Баланс аккаунта: ${web3.utils.fromWei(balanceWei, 'ether')} ETH`);

        // Отправка транзакции
        // В Hardhat можно отправлять на любой другой аккаунт из списка
        const toAddress = '0x70997970C51812dc3A010C7d01b50e0d17dc79C8'; // Аккаунт #1
        const tx = {
            from: account.address,
            to: toAddress,
            value: web3.utils.toWei('1', 'ether'), // Отправляем 1 ETH
            gas: 21000,
            gasPrice: await web3.eth.getGasPrice(),
            // Для локальной сети можно не указывать chainId, Hardhat сам подхватит,
            // но для надежности лучше добавить:
            chainId: 31337 
        };

        console.log('Отправка транзакции...');
        const signedTx = await web3.eth.accounts.signTransaction(tx, privateKey);
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
        
        console.log(`✅ Транзакция успешна! Хэш: ${receipt.transactionHash}`);
        
        // Проверяем, что баланс получателя изменился
        const newBalanceWei = await web3.eth.getBalance(toAddress);
        console.log(`Новый баланс получателя: ${web3.utils.fromWei(newBalanceWei, 'ether')} ETH`);

    } catch (error) {
        console.error('❌ Ошибка:', error.message);
    }
}

run();
