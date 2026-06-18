# memory.py - Работа с памятью через ctypes и pywin32
import ctypes
import ctypes.wintypes
from ctypes import byref, sizeof
import os
import json
from pathlib import Path

# Загрузка offsets
OFFSETS_PATH = Path(__file__).parent / "offsets.json"
with open(OFFSETS_PATH) as f:
    OFFSETS = json.load(f)

# Константы Windows
PROCESS_VM_READ = 0x0010
PROCESS_VM_WRITE = 0x0020
PROCESS_VM_OPERATION = 0x0008
PROCESS_ALL_ACCESS = 0x1F0FFF

# Инициализация ctypes
kernel32 = ctypes.windll.kernel32
user32 = ctypes.windll.user32

def get_process_handle(pid):
    """Открывает процесс по PID с правами на чтение/запись"""
    handle = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    if not handle:
        raise Exception(f"Не удалось открыть процесс PID {pid}")
    return handle

def read_memory(handle, address, size=4):
    """Читает память по адресу и возвращает int"""
    buffer = ctypes.create_string_buffer(size)
    bytes_read = ctypes.c_ulong(0)
    if kernel32.ReadProcessMemory(handle, address, buffer, size, byref(bytes_read)):
        if size == 4:
            return int.from_bytes(buffer.raw[:4], byteorder='little')
        elif size == 8:
            return int.from_bytes(buffer.raw[:8], byteorder='little')
        else:
            return buffer.raw
    return None

def write_memory(handle, address, value, size=4):
    """Записывает значение в память"""
    if size == 4:
        data = value.to_bytes(4, byteorder='little')
    elif size == 8:
        data = value.to_bytes(8, byteorder='little')
    else:
        data = value.encode('utf-16le') if isinstance(value, str) else bytes(value)
    bytes_written = ctypes.c_ulong(0)
    result = kernel32.WriteProcessMemory(handle, address, data, len(data), byref(bytes_written))
    return result != 0

def close_handle(handle):
    kernel32.CloseHandle(handle)

# Утилита для получения PID по имени процесса (заглушка)
def get_pid_by_name(process_name):
    # В реальном коде используется tlhelp32 или psutil
    # Здесь возвращаем фиктивный PID для демонстрации
    return 12345  # Замените на реальную логику
