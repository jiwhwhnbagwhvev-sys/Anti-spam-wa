    # colors.py
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_BLUE = "\033[94m"
COLOR_CYAN = "\033[96m"      # BIRU MUDA
COLOR_YELLOW = "\033[93m"
COLOR_MAGENTA = "\033[95m"
COLOR_RESET = "\033[0m"

def print_info(msg):
    print(f"{COLOR_CYAN}[INFO]{COLOR_RESET} {msg}")

def print_success(msg):
    print(f"{COLOR_GREEN}[SUCCESS]{COLOR_RESET} {msg}")

def print_error(msg):
    print(f"{COLOR_RED}[ERROR]{COLOR_RESET} {msg}")

def print_warning(msg):
    print(f"{COLOR_YELLOW}[WARN]{COLOR_RESET} {msg}")
