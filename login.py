import sys
import time
import os

# pastikan MODULES terbaca
sys.path.append(os.path.join(os.path.dirname(__file__), "MODULES"))

from config import (
    USERNAME,
    PASSWORD,
    MAX_LOGIN_ATTEMPT,
    LOCK_TIME_SECONDS,
    COLOR_RED,
    COLOR_BLUE,
    COLOR_GREEN,
    COLOR_RESET,
    SPINNER,
    LOADING_SPEED
)
from colors import print_success, print_error, print_info


def clear():
    os.system("clear")


def terminator_logo():
    print(COLOR_BLUE)
    print(r"""
████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ████████╗ ██████╗ ██████╗ 
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
   ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║   ██║   ██║   ██║██████╔╝
   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║   ██║   ██║   ██║██╔══██╗
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║   ██║   ╚██████╔╝██║  ██║
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
    """)
    print(COLOR_RESET)


def loading(text="Memverifikasi"):
    for i in range(20):
        spin = SPINNER[i % len(SPINNER)]
        print(f"\r{text} {spin}", end="", flush=True)
        time.sleep(LOADING_SPEED)
    print()


def login():
    attempt = 0

    while attempt < MAX_LOGIN_ATTEMPT:
        clear()
        terminator_logo()

        print_info("LOGIN ANTI SPAM TERMINATOR\n")
        user = input("Username : ").strip()
        pwd = input("Password : ").strip()

        loading("Memverifikasi")

        if user == USERNAME and pwd == PASSWORD:
            print_success("Login berhasil!")
            time.sleep(1)
            os.system("PYTHONPATH=MODULES python menu.py")
            sys.exit(0)
        else:
            attempt += 1
            sisa = MAX_LOGIN_ATTEMPT - attempt
            print_error(f"Login gagal! Sisa percobaan: {sisa}")
            time.sleep(2)

    print_error(f"Terlalu banyak percobaan! Akun dikunci {LOCK_TIME_SECONDS} detik.")
    time.sleep(LOCK_TIME_SECONDS)
    sys.exit(1)


if __name__ == "__main__":
    login()
