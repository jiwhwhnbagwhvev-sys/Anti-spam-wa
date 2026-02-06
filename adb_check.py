import os
import subprocess
from colors import print_info, print_success, print_error
from config import ADB_REQUIRED, DEBUG_MODE

def check_adb():
    """
    Mengecek apakah ADB tersedia dan HP tersambung
    """
    if not ADB_REQUIRED:
        print_info("ADB tidak dibutuhkan, melewati pengecekan...")
        return True

    try:
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
        lines = result.stdout.strip().split("\n")
        devices = [line for line in lines if "\tdevice" in line]

        if len(devices) == 0:
            print_error("Tidak ada perangkat Android tersambung!")
            print_info("Pastikan Developer Options & USB Debugging aktif")
            return False
        else:
            print_success(f"Terhubung dengan perangkat: {devices[0].split()[0]}")
            return True
    except FileNotFoundError:
        print_error("ADB tidak ditemukan! Install adb di Termux / sistem Anda")
        return False
    except Exception as e:
        if DEBUG_MODE:
            print_error(f"Error cek ADB: {e}")
        return False

# ===== FUNSI BANTU =====
def adb_shell(command):
    """
    Menjalankan perintah adb shell
    """
    try:
        result = subprocess.run(["adb", "shell"] + command.split(), capture_output=True, text=True)
        if DEBUG_MODE:
            print(f"ADB Output: {result.stdout.strip()}")
        return result.stdout.strip()
    except Exception as e:
        print_error(f"Gagal menjalankan adb shell: {e}")
        return None

if __name__ == "__main__":
    if check_adb():
        print_success("ADB siap digunakan untuk fitur Anti-Spam Real")
    else:
        print_error("ADB tidak tersedia. Beberapa fitur tidak bisa dijalankan")
