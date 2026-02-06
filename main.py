import os
import time
from anti_spam_core import single_target, mass_target, view_targets
from dnd_control import toggle_dnd
from silence_calls import toggle_silence_calls
from whatsapp_guard import toggle_whatsapp_guard, show_status as wa_status
from colors import (
    print_info, print_success, print_error,
    COLOR_BLUE, COLOR_RESET
)

# ==============================
# CLEAR TERMINAL
# ==============================
def clear():
    os.system("clear")

# ==============================
# LOGO TERMINATOR (SAJA)
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
    print(COLOR_BLUE + "                 ANTI SPAM TERMINATOR" + COLOR_RESET)
    print("=" * 60)
    print()

# ==============================
# MENU UTAMA (BIRU)
# ==============================
def main_menu():
    while True:
        clear()
        logo_terminator()
        print(COLOR_BLUE + "1. Anti Spam" + COLOR_RESET)
        print(COLOR_BLUE + "2. Lihat Target Spam" + COLOR_RESET)
        print(COLOR_BLUE + "3. Toggle Proteksi Cepat" + COLOR_RESET)
        print(COLOR_BLUE + "4. Exit" + COLOR_RESET)
        print()
        choice = input("Pilih menu: ").strip()

        if choice == "1":
            anti_spam_menu()
        elif choice == "2":
            view_targets()
            input("Tekan Enter untuk kembali...")
        elif choice == "3":
            quick_toggle()
            input("Tekan Enter untuk kembali...")
        elif choice == "4":
            print_info("Keluar program...")
            time.sleep(1)
            break
        else:
            print_error("Pilihan tidak valid!")
            time.sleep(1)

# ==============================
# ANTI SPAM MENU
# ==============================
def anti_spam_menu():
    while True:
        clear()
        logo_terminator()
        print(COLOR_BLUE + "ANTI SPAM" + COLOR_RESET)
        print(COLOR_BLUE + "1. Single Target" + COLOR_RESET)
        print(COLOR_BLUE + "2. Massal Target" + COLOR_RESET)
        print(COLOR_BLUE + "3. Kembali" + COLOR_RESET)
        print()
        choice = input("Pilih menu: ").strip()

        if choice == "1":
            number = input("Masukkan nomor target: ").strip()
            single_target(number)
            input("Tekan Enter untuk kembali...")
        elif choice == "2":
            numbers = input("Masukkan nomor target (pisahkan koma): ").strip().split(",")
            mass_target([n.strip() for n in numbers])
            input("Tekan Enter untuk kembali...")
        elif choice == "3":
            break
        else:
            print_error("Pilihan tidak valid!")
            time.sleep(1)

# ==============================
# QUICK TOGGLE PROTEKSI
# ==============================
def quick_toggle():
    clear()
    logo_terminator()
    print_info("Toggle cepat semua proteksi...")
    toggle_dnd()
    toggle_silence_calls()
    toggle_whatsapp_guard()
    wa_status()
    print_success("Toggle selesai.")

# ==============================
# ENTRY POINT
# ==============================
if __name__ == "__main__":
    clear()
    main_menu()
