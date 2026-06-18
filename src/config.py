# config.py - Конфигурация для AgenticDeFi Trainer
import os

# Настройки подключения к процессу (пример)
PROCESS_NAME = "AgenticDeFi.exe"   # Имя процесса игры/приложения
BASE_ADDRESS = 0x12345678          # Базовый адрес (будет загружен из offsets.json)

# Настройки API (для демонстрации)
API_KEYS = {
    "news_api": "YOUR_NEWS_API_KEY",
    "price_oracle": "YOUR_ORACLE_KEY"
}

# Параметры кошелька (x402)
WALLET_CONFIG = {
    "network": "Ethereum",
    "stablecoin": "USDC",
    "gas_limit": 300000
}

# Настройки безопасности
SECURE_MODE = True
ALLOWED_CONTRACTS = ["0x...", "0x..."]
