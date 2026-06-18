# utils.py - Вспомогательные функции
import time
import random
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def delay(seconds=None):
    """Имитация задержки для избежания детекта"""
    if seconds is None:
        seconds = random.uniform(0.1, 0.5)
    time.sleep(seconds)

def log_action(action, success=True):
    """Логирование действий"""
    status = "SUCCESS" if success else "FAILED"
    logging.info(f"{action} -> {status}")

def safe_hex(value):
    """Преобразование в hex для отображения"""
    return hex(value) if isinstance(value, int) else str(value)
