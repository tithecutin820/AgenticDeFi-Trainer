# main.py - Точка входа с горячими клавишами (F1-F8)
import sys
import time
import threading
try:
    import keyboard  # для обработки горячих клавиш
except ImportError:
    print("Установка keyboard...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "keyboard"])
    import keyboard

from trainer import AgenticTrainer

trainer = AgenticTrainer()

def on_f1():
    print("[F1] Подключение кошелька...")
    trainer.connect_wallet()

def on_f2():
    print("[F2] Авто-бридж и доходность...")
    trainer.auto_bridge_and_yield()

def on_f3():
    print("[F3] Динамическое ребалансирование...")
    trainer.dynamic_rebalance()

def on_f4():
    print("[F4] Исполнение интента...")
    trainer.intent_execution()

def on_f5():
    print("[F5] Обработка новостей...")
    trainer.process_news()

def on_f6():
    print("[F6] Координация роя...")
    trainer.swarm_coordination()

def on_f7():
    print("[F7] Самовыполняющийся контракт...")
    trainer.execute_smart_contract()

def on_f8():
    print("[F8] Управление казначейством...")
    trainer.treasury_management()

def main():
    print("=== AgenticDeFi Trainer ===")
    print("Нажмите F1-F8 для выполнения функций.")
    print("Нажмите ESC для выхода.")
    keyboard.add_hotkey('f1', on_f1)
    keyboard.add_hotkey('f2', on_f2)
    keyboard.add_hotkey('f3', on_f3)
    keyboard.add_hotkey('f4', on_f4)
    keyboard.add_hotkey('f5', on_f5)
    keyboard.add_hotkey('f6', on_f6)
    keyboard.add_hotkey('f7', on_f7)
    keyboard.add_hotkey('f8', on_f8)
    keyboard.wait('esc')
    trainer.disconnect()
    print("Выход.")

if __name__ == "__main__":
    main()
