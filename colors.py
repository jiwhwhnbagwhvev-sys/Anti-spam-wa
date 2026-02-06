# ===============================
# COLORS & STYLE TERMINAL
# ===============================
# Digunakan di semua menu & banner

# WARNA DASAR
BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

# WARNA TERANG / BOLD
BOLD_BLACK   = "\033[1;30m"
BOLD_RED     = "\033[1;31m"
BOLD_GREEN   = "\033[1;32m"
BOLD_YELLOW  = "\033[1;33m"
BOLD_BLUE    = "\033[1;34m"
BOLD_MAGENTA = "\033[1;35m"
BOLD_CYAN    = "\033[1;36m"
BOLD_WHITE   = "\033[1;37m"

# BACKGROUND WARNA
BG_BLACK   = "\033[40m"
BG_RED     = "\033[41m"
BG_GREEN   = "\033[42m"
BG_YELLOW  = "\033[43m"
BG_BLUE    = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN    = "\033[46m"
BG_WHITE   = "\033[47m"

# RESET STYLE
RESET_ALL = "\033[0m"

# EFFECTS
UNDERLINE      = "\033[4m"
REVERSED       = "\033[7m"
BLINK          = "\033[5m"
DIM            = "\033[2m"
BOLD           = "\033[1m"

# ===== FUNSI BANTU =====
def colored(text, color=WHITE, bold=False, underline=False):
    style = ""
    if bold:
        style += "\033[1m"
    if underline:
        style += "\033[4m"
    return f"{style}{color}{text}{RESET_ALL}"

def print_info(msg):
    print(colored(f"[INFO] {msg}", CYAN, bold=True))

def print_success(msg):
    print(colored(f"[SUCCESS] {msg}", GREEN, bold=True))

def print_error(msg):
    print(colored(f"[ERROR] {msg}", RED, bold=True))

def print_warning(msg):
    print(colored(f"[WARNING] {msg}", YELLOW, bold=True))

def print_debug(msg):
    from config import DEBUG_MODE
    if DEBUG_MODE:
        print(colored(f"[DEBUG] {msg}", MAGENTA, bold=True))
