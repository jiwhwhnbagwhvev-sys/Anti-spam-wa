import os
import time
from colors import print_info, print_success, print_error, print_warning, colored
from config import COLOR_BLUE, COLOR_RESET
from anti_spam_core import single_target, mass_target, view_targets

def clear_screen():
    os.system("clear")

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
    print(COLOR_BLUE + "             TERMINATOR MENU" + COLOR_RESET)
    print("="*50)

def main_menu():
    while True:
        clear_screen()
        logo_terminator()
        print(colored("1. Anti Spam", COLOR_BLUE, bold=True))
        print(colored("2. Lihat Target Spam", COLOR_BLUE, bold=True))
        print(colored("3. Exit", COLOR_BLUE, bold=True))
        print()
        choice = input("Pilih menu: ")

        if choice == "1":
            spam_menu()
        elif choice == "2":
            view_targets()
            input("\nTekan Enter untuk kembali...")
        elif choice == "3":
            print_success("Keluar dari program...")
            break
        else:
            print_warning("Pilihan tidak valid!")
            time.sleep(1)

def spam_menu():
    clear_screen()
    logo_terminator()
    print(colored("1. Single Target", COLOR_BLUE, bold=True))
    print(colored("2. Massal Target", COLOR_BLUE, bold=True))
    print(colored("3. Kembali", COLOR_BLUE, bold=True))
    print()
    choice = input("Pilih menu: ")

    if choice == "1":
        single_target()
    elif choice == "2":
        mass_target()
    elif choice == "3":
        return
    else:
        print_warning("Pilihan tidak valid!")
        time.sleep(1)

if __name__ == "__main__":
    main_menu()
