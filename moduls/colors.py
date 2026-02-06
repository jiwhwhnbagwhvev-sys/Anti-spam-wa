from config import COLOR_RESET, COLOR_RED, COLOR_GREEN, COLOR_YELLOW, COLOR_BLUE, COLOR_MAGENTA, COLOR_CYAN, COLOR_WHITE, DEBUG_MODE

# ==============================
# Fungsi Print Warna
# ==============================
def colored(text, color_code, bold=False):
    """
    Menghasilkan text berwarna untuk terminal
    """
    style = "\033[1m" if bold else ""
    return f"{style}{color_code}{text}{COLOR_RESET}"

def print_info(msg):
    print(colored(f"[INFO] {msg}", COLOR_BLUE, bold=True))

def print_success(msg):
    print(colored(f"[SUCCESS] {msg}", COLOR_GREEN, bold=True))

def print_warning(msg):
    print(colored(f"[WARNING] {msg}", COLOR_YELLOW, bold=True))

def print_error(msg):
    print(colored(f"[ERROR] {msg}", COLOR_RED, bold=True))

def print_debug(msg):
    if DEBUG_MODE:
        print(colored(f"[DEBUG] {msg}", COLOR_MAGENTA, bold=True))

def print_cyan(msg):
    print(colored(msg, COLOR_CYAN))

def print_white(msg):
    print(colored(msg, COLOR_WHITE))

def print_blue(msg):
    print(colored(msg, COLOR_BLUE))

def print_red(msg):
    print(colored(msg, COLOR_RED))

def print_green(msg):
    print(colored(msg, COLOR_GREEN))

def print_yellow(msg):
    print(colored(msg, COLOR_YELLOW))

# ==============================
# Banner / Header Helper
# ==============================
def banner(title="ANTI-SPAM REAL"):
    print_blue("="*60)
    print_blue(f"{title.center(60)}")
    print_blue("="*60)
