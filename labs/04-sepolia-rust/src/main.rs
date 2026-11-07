use alloy::{
    network::TransactionBuilder,
    primitives::U256,
    providers::{Provider, ProviderBuilder},
    rpc::types::TransactionRequest,
    signers::local::PrivateKeySigner,
};
use dotenv::dotenv;
use std::env;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    dotenv().ok();

    let rpc_url = env::var("RPC_URL")?;
    let private_key = env::var("PRIVATE_KEY")?;
    let to_address = env::var("TO_ADDRESS")?.parse()?;

    // 1. Подключаемся к Sepolia
        // 1. Сначала создаем signer (кошелек) из приватного ключа
        let signer: PrivateKeySigner = private_key.parse()?;
        // 2. Создаем провайдер и привязываем к нему кошелек через .wallet()
        let provider = ProviderBuilder::new()
        .wallet(signer.clone()) // <-- Вот это добавляет управление nonce
        .connect_http(rpc_url.parse()?);
    
    let block_number = provider.get_block_number().await?;
    let chain_id = provider.get_chain_id().await?;
    println!("✅ Подключено к Sepolia. Блок: {}, Chain ID: {}", block_number, chain_id);

    // 2. Загружаем кошелек
    let signer: PrivateKeySigner = private_key.parse()?;
    let alice = signer.address();
    println!("Наш адрес: {}", alice);

    let balance = provider.get_balance(alice).await?;
    println!("Баланс: {} ETH", alloy::primitives::utils::format_ether(balance));

    // 3. Отправляем транзакцию
    let tx = TransactionRequest::default()
        .with_to(to_address)
        .with_value(U256::from(1_000_000_000_000_000u64)) // 0.001 ETH в Wei
        .with_chain_id(chain_id);

    println!("Отправка транзакции...");
    
    // Подписываем и отправляем
         let pending_tx = provider.send_transaction(tx).await?;
         let tx_hash = pending_tx.tx_hash();
    println!("✅ Транзакция отправлена! Хэш: {:?}", tx_hash);
    println!("🔗 https://sepolia.etherscan.io/tx/{:?}", tx_hash);

    Ok(())
}
