    # ==============================
# IMPORT WARNA DARI CONFIG
# ==============================
from config import COLOR_RED, COLOR_GREEN, COLOR_BLUE, COLOR_YELLOW, COLOR_RESET

# ==============================
# FUNGSI PRINT WARNA
# ==============================
def print_success(text):
    """Print text berwarna hijau"""
    print(f"{COLOR_GREEN}{text}{COLOR_RESET}")

def print_error(text):
    """Print text berwarna merah"""
    print(f"{COLOR_RED}{text}{COLOR_RESET}")

def print_info(text):
    """Print text berwarna biru"""
    print(f"{COLOR_BLUE}{text}{COLOR_RESET}")

def print_warning(text):
    """Print text berwarna kuning"""
    print(f"{COLOR_YELLOW}{text}{COLOR_RESET}")

# ==============================
# VARIASI WARNA BOLD
# ==============================
BOLD_RED = "\033[1;91m"
BOLD_GREEN = "\033[1;92m"
BOLD_BLUE = "\033[1;94m"
BOLD_YELLOW = "\033[1;93m"

# ==============================
# PRINT BOLD
# ==============================
def print_bold_red(text):
    print(f"{BOLD_RED}{text}{COLOR_RESET}")

def print_bold_green(text):
    print(f"{BOLD_GREEN}{text}{COLOR_RESET}")

def print_bold_blue(text):
    print(f"{BOLD_BLUE}{text}{COLOR_RESET}")

def print_bold_yellow(text):
    print(f"{BOLD_YELLOW}{text}{COLOR_RESET}")

# ==============================
# PRINT WARNA + PREFIX SYMBOL
# ==============================
def print_success_symbol(text):
    print(f"{COLOR_GREEN}✔ {text}{COLOR_RESET}")

def print_error_symbol(text):
    print(f"{COLOR_RED}✖ {text}{COLOR_RESET}")

def print_info_symbol(text):
    print(f"{COLOR_BLUE}ℹ {text}{COLOR_RESET}")

def print_warning_symbol(text):
    print(f"{COLOR_YELLOW}⚠ {text}{COLOR_RESET}")
