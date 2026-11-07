// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "forge-std/Test.sol";

// Интерфейс для работы с токеном (нам нужна только функция balanceOf)
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}

contract ForkTest is Test {
    // Официальный адрес контракта USDC в сети Sepolia [citation:2][citation:7]
    address constant USDC_SEPOLIA = 0x1c7D4B196Cb0C7B01d743Fbc6116a902379C7238;
    
    // Адрес кошелька, у которого точно есть USDC в Sepolia 
    // (взят из примеров тестов Foundry) [citation:8]
    address constant WALLET = 0x75C0c372da875a4Fc78E8A37f58618a6D18904e8; 

    IERC20 usdc;

    function setUp() public {
        // 1. СОЗДАЕМ ФОРК СЕТИ SEPOLIA
        vm.createSelectFork("sepolia");

        // 2. Подключаемся к контракту USDC
        usdc = IERC20(USDC_SEPOLIA);
    }

    function testReadBalance() public view {
        // 3. Читаем баланс реального контракта в форкнутой сети
        uint256 balance = usdc.balanceOf(WALLET);
        
        // Выводим результат в лог
        console.log("USDC balance of:", WALLET);
        console.log("Raw value (smallest units):", balance);
        
        // 4. Проверяем, что баланс больше нуля
        assertGt(balance, 0);
    }
}

