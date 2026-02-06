import os
import time
import subprocess
from colors import print_info, print_success, print_error, print_warning
from config import STATUS_WHATSAPP_GUARD, DEBUG_MODE, COLOR_BLUE, COLOR_RESET

# ==============================
# LOGO TERMINATOR
# ==============================
def logo_terminator():
    logo = [
        "████████╗██████╗ ██████╗ ███╗   ███╗ █████╗ ██████╗ ███████╗",
        "╚══██╔══╝██╔══██╗██╔══██╗████╗ ████║██╔══██╗██╔══██╗██╔════╝",
        "   ██║   ██████╔╝██████╔╝██╔████╔██║███████║██████╔╝█████╗  ",
        "   ██║   ██╔═══╝ ██╔═══╝ ██║╚██╔╝██║██╔══██║██╔═══╝ ██╔══╝  ",
        "   ██║   ██║     ██║     ██║ ╚═╝ ██║██║  ██║██║     ███████╗",
        "   ╚═╝   ╚═╝     ╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝"
    ]
    for line in logo:
        print(COLOR_BLUE + line + COLOR_RESET)
    print(COLOR_BLUE + "           WHATSAPP GUARD ACTIVE" + COLOR_RESET)
    print("="*60)
    print()

# ==============================
# WHATSAPP GUARD - ANTI SPAM
# ==============================
def adb_shell(command):
    try:
        result = subprocess.run(["adb", "shell"] + command.split(), capture_output=True, text=True)
        if DEBUG_MODE:
            print(f"[DEBUG] ADB Output: {result.stdout.strip()}")
        return result.stdout.strip()
    except Exception as e:
        print_error(f"Gagal menjalankan adb shell: {e}")
        return None

def enable_whatsapp_guard():
    try:
        adb_shell("settings put global zen_mode 1")  # DND total
        adb_shell("cmd notification suspend_package com.whatsapp")  # pause notifikasi WA
        global STATUS_WHATSAPP_GUARD
        STATUS_WHATSAPP_GUARD = True
        print_success("WhatsApp Guard AKTIF - Semua panggilan spam & notifikasi dibungkam")
    except Exception as e:
        print_error(f"Gagal mengaktifkan WhatsApp Guard: {e}")

def disable_whatsapp_guard():
    try:
        adb_shell("settings put global zen_mode 0")  # matikan DND
        adb_shell("cmd notification unsuspend_package com.whatsapp")  # aktifkan notifikasi WA
        global STATUS_WHATSAPP_GUARD
        STATUS_WHATSAPP_GUARD = False
        print_success("WhatsApp Guard NONAKTIF - Notifikasi & panggilan WA normal")
    except Exception as e:
        print_error(f"Gagal menonaktifkan WhatsApp Guard: {e}")

def toggle_whatsapp_guard():
    if STATUS_WHATSAPP_GUARD:
        disable_whatsapp_guard()
    else:
        enable_whatsapp_guard()

def show_status():
    status = "AKTIF" if STATUS_WHATSAPP_GUARD else "NONAKTIF"
    print_info(f"Status WhatsApp Guard: {status}")

# ==============================
# Single & Mass Target Protection
# ==============================
def protect_single_target(number):
    try:
        adb_shell(f"echo 'Blacklist WA {number}' >> /sdcard/ANTI_SPAM_REAL/logs/whatsapp_blacklist.log")
        print_success(f"Nomor {number} berhasil ditambahkan ke proteksi WA")
    except Exception as e:
        print_error(f"Gagal menambahkan nomor {number}: {e}")

def protect_mass_targets(number_list):
    if not isinstance(number_list, list):
        print_warning("Input harus berupa list nomor")
        return
    for num in number_list:
        protect_single_target(num)
        time.sleep(0.2)

# ==============================
# Logger panggilan WA spam
# ==============================
def log_whatsapp_call(number, status="Blocked"):
    try:
        logfile = "/sdcard/ANTI_SPAM_REAL/logs/whatsapp_calls.log"
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        adb_shell(f"echo '{timestamp} | {number} | {status}' >> {logfile}")
        if DEBUG_MODE:
            print(f"[DEBUG] Log WA: {timestamp} | {number} | {status}")
    except Exception as e:
        print_error(f"Gagal mencatat log WA: {e}")

def auto_detect_and_block(calls_list):
    for call in calls_list:
        number = call.get("number")
        spam_flag = call.get("spam", False)
        if spam_flag:
            protect_single_target(number)
            log_whatsapp_call(number)
            print_info(f"Spam WA dari {number} berhasil diblokir")
        else:
            print_info(f"WA normal dari {number}, tidak diblokir")

# ==============================
# TEST PANJANG REAL
# ==============================
if __name__ == "__main__":
    logo_terminator()  # tampilkan logo TERMINATOR di atas
    print_info("Menjalankan WhatsApp Guard Test Panjang...")
    enable_whatsapp_guard()
    show_status()
    protect_single_target("+6281234567890")
    protect_mass_targets(["+628111111111", "+628222222222", "+628333333333"])
    auto_detect_and_block([
        {"number": "+6281234567890", "spam": True},
        {"number": "+628444444444", "spam": False},
        {"number": "+628222222222", "spam": True}
    ])
    time.sleep(2)
    show_status()
    disable_whatsapp_guard()
    show_status()
