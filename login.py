import os
import time
import getpass
from colors import print_success, print_error, print_info
from config import USERNAME, PASSWORD, MAX_LOGIN_ATTEMPT, LOCK_TIME_SECONDS, COLOR_RED, COLOR_BLUE, COLOR_RESET, SPINNER, LOADING_SPEED

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
        print(COLOR_RED + line + COLOR_RESET)
    print(COLOR_BLUE + "             TERMINATOR LOGIN" + COLOR_RESET)
    print()

def loading_animation(message="Memeriksa kredensial..."):
    import sys
    for i in range(3):
        for frame in SPINNER:
            sys.stdout.write(f"\r{message} {frame}")
            sys.stdout.flush()
            time.sleep(LOADING_SPEED)
    sys.stdout.write("\r" + message + " ✔\n")

def login():
    clear_screen()
    logo_terminator()
    print_info("Silahkan login untuk mengakses menu Anti-Spam Real\n")

    attempt = 0
    while attempt < MAX_LOGIN_ATTEMPT:
        username_input = input("Username: ")
        password_input = getpass.getpass("Password: ")

        loading_animation("Memverifikasi akun...")

        if username_input == USERNAME and password_input == PASSWORD:
            print_success("Login berhasil!")
            time.sleep(1)
            return True
        else:
            attempt += 1
            print_error(f"Login gagal! Sisa percobaan: {MAX_LOGIN_ATTEMPT - attempt}")
            if attempt >= MAX_LOGIN_ATTEMPT:
                print_error(f"Terlalu banyak percobaan! Kunci sementara {LOCK_TIME_SECONDS} detik...")
                time.sleep(LOCK_TIME_SECONDS)
                attempt = 0  # reset attempt setelah timeout

def main():
    if login():
        os.system("python menu.py")  # lanjut ke menu utama

if __name__ == "__main__":
    main()
