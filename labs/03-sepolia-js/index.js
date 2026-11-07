import { Web3 } from 'web3';
import dotenv from 'dotenv';
dotenv.config();

const web3 = new Web3(process.env.RPC_URL);

async function run() {
    try {
        const blockNumber = await web3.eth.getBlockNumber();
        const chainId = await web3.eth.getChainId();
        console.log(`✅ Подключено к Sepolia. Блок: ${blockNumber}, Chain ID: ${chainId} (должен быть 11155111)`);

        const account = web3.eth.accounts.privateKeyToAccount(process.env.PRIVATE_KEY);
        web3.eth.accounts.wallet.add(account);
        console.log(`Наш адрес: ${account.address}`);

        const balanceWei = await web3.eth.getBalance(account.address);
        console.log(`Баланс: ${web3.utils.fromWei(balanceWei, 'ether')} ETH`);

                const tx = {
            from: account.address,
            to: process.env.TO_ADDRESS,
            value: web3.utils.toWei('0.001', 'ether'),
            gasPrice: await web3.eth.getGasPrice(), // <-- Явно задаем цену газа
            chainId: 11155111
            // Убрали "gas: 21000", чтобы web3.js сам рассчитал лимит (он сделает это корректно)
                };

        console.log('Отправка транзакции...');
        const signedTx = await web3.eth.accounts.signTransaction(tx, process.env.PRIVATE_KEY);
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
        
        console.log(`✅ Успех! Хэш: ${receipt.transactionHash}`);
        console.log(`🔗 https://sepolia.etherscan.io/tx/${receipt.transactionHash}`);

    } catch (error) {
        console.error('❌ Ошибка:', error.message);
    }
}
run();
