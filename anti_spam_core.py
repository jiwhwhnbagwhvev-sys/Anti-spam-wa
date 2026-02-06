import time
import sys
from colors import (
    print_info, print_success, print_error, print_warning,
    COLOR_CYAN, COLOR_BLUE, COLOR_GREEN, COLOR_MAGENTA, COLOR_YELLOW, COLOR_RESET
)
from spam_logger import log_spam, view_logs, search_number

# ==============================
# LOGO TERMINATOR (BIRU MUDA)
# ==============================
def logo_terminal():
    logo = [
        "████████╗██████╗ ██████╗ ███╗   ███╗",
        "╚══██╔══╝██╔══██╗██╔══██╗████╗ ████║",
        "   ██║   ██████╔╝██████╔╝██╔████╔██║",
        "   ██║   ██╔═══╝ ██╔═══╝ ██║╚██╔╝██║",
        "   ██║   ██║     ██║     ██║ ╚═╝ ██║",
        "   ╚═╝   ╚═╝     ╚═╝     ╚═╝     ╚═╝",
        "           R I O _ V I P 2 . 0"
    ]
    print(COLOR_CYAN + "="*70 + COLOR_RESET)
    for l in logo:
        print(COLOR_CYAN + l.center(70) + COLOR_RESET)
    print(COLOR_CYAN + "="*70 + COLOR_RESET)
    print()

# ==============================
# DETEKSI OPERATOR
# ==============================
def detect_operator(number: str):
    n = number.replace("+62", "0").replace(" ", "")
    prefixes = {
        "Telkomsel": ["0811","0812","0813","0821","0822","0823","0851","0852","0853"],
        "Indosat": ["0814","0815","0816","0855","0856","0857","0858"],
        "XL": ["0817","0818","0819","0859","0877","0878"],
        "Tri": ["0895","0896","0897","0898","0899"],
        "Smartfren": ["0881","0882","0883","0884","0885","0886","0887","0888","0889"]
    }
    for op, prefs in prefixes.items():
        for p in prefs:
            if n.startswith(p):
                return op
    return "Unknown"

# ==============================
# LOADING ANIMASI KEREN
# ==============================
def rainbow_loading(text, duration=3):
    frames = [" >", ">>", ">>>", ">>>>", "<<<", "<<", "<"]
    colors = [COLOR_CYAN, COLOR_BLUE, COLOR_MAGENTA, COLOR_YELLOW, COLOR_GREEN]
    start = time.time()
    i = 0
    while time.time() - start < duration:
        c = colors[i % len(colors)]
        f = frames[i % len(frames)]
        sys.stdout.write(
            f"\r{c}{f} Verifikasi {text}{COLOR_RESET}   "
        )
        sys.stdout.flush()
        time.sleep(0.12)
        i += 1
    print()

# ==============================
# SINGLE TARGET (KEREN)
# ==============================
def single_target():
    logo_terminal()
    number = input("Masukkan nomor target : ").strip()

    operator = detect_operator(number)
    print_info(f"Status Verifikasi Nomor")
    print(f"{COLOR_CYAN}Nomor     : {number}{COLOR_RESET}")
    print(f"{COLOR_CYAN}Operator  : {operator}{COLOR_RESET}")
    print()

    rainbow_loading(number, duration=4)

    # simulasi proteksi + logging
    log_spam(number, source=operator, type_spam="ALL", status="PROTECTED")

    print_success("Proteksi aktif untuk nomor di atas")
    input("Tekan Enter untuk kembali...")

# ==============================
# MASS TARGET
# ==============================
def mass_target():
    logo_terminal()
    data = input("Masukkan nomor (pisah koma): ")
    nums = [x.strip() for x in data.split(",") if x.strip()]

    for n in nums:
        op = detect_operator(n)
        rainbow_loading(n, duration=2)
        log_spam(n, source=op, type_spam="ALL", status="PROTECTED")

    print_success("Proteksi massal selesai")
    input("Tekan Enter untuk kembali...")

# ==============================
# VIEW TARGETS
# ==============================
def view_targets():
    logo_terminal()
    print_info("Daftar Log Target Spam")
    view_logs()
    input("Tekan Enter untuk kembali...")
