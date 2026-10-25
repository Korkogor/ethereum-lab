import { Web3 } from 'web3';

// Подключаемся к локальной сети Hardhat
const web3 = new Web3('http://127.0.0.1:8545');

// Вставьте сюда адрес контракта из Remix
const contractAddress = '0x5FbDB2315678afecb367f032d93F642f64180aa3';

// ABI — это «инструкция» для JavaScript, описывающая функции контракта
const contractABI = [
  {
    "inputs": [],
    "name": "message",
    "outputs": [{"internalType": "string", "name": "", "type": "string"}],
    "stateMutability": "view",
    "type": "function"
  }
];

async function main() {
  const contract = new web3.eth.Contract(contractABI, contractAddress);
  const message = await contract.methods.message().call();
  console.log('Сообщение из блокчейна:', message);
}
main();
