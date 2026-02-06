import os

# ==============================
# KONFIGURASI GLOBAL
# ==============================
DEBUG_MODE = True  # True untuk debug output lengkap
ADB_REQUIRED = True  # ADB wajib untuk fitur nyata Anti-Spam

# ==============================
# PATH / FILE
# ==============================
BASE_DIR = os.path.expanduser("~/ANTI-SPAM-REAL")
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

SESSION_FILE = os.path.join(BASE_DIR, "session.dat")
LOG_SPAM_FILE = os.path.join(LOG_DIR, "spam.log")
WHATSAPP_LOG_FILE = os.path.join(LOG_DIR, "whatsapp_calls.log")

# ==============================
# STATUS GLOBAL
# ==============================
STATUS_DND = False
STATUS_SILENCE_CALLS = False
STATUS_WHATSAPP_GUARD = False

# ==============================
# WARNA TERMINAL
# ==============================
COLOR_RESET = "\033[0m"
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_MAGENTA = "\033[95m"
COLOR_CYAN = "\033[96m"
COLOR_WHITE = "\033[97m"

# ==============================
# LOGIN DEFAULT
# ==============================
USERNAME = "Rio_V2-antispam"
PASSWORD = "Rio_V2-2026"

# ==============================
# WA / SMS / CALL SETTINGS
# ==============================
DEFAULT_CALL_BLOCK = True
DEFAULT_SMS_BLOCK = True
DEFAULT_WA_BLOCK = True

# ==============================
# UTILITY / FLAG
# ==============================
ALLOW_SINGLE_TARGET = True
ALLOW_MASS_TARGET = True
ALLOW_LOG_VIEW = True
ALLOW_FULL_PROTECTION = True

# ==============================
# LOG / DEBUG SETTINGS
# ==============================
ENABLE_LOGGING = True
LOG_LEVEL = "DEBUG"  # DEBUG, INFO, WARN, ERROR

# ==============================
# FUNGSI BANTU
# ==============================
def print_debug(msg):
    if DEBUG_MODE:
        print(f"[DEBUG] {msg}")

def print_info(msg):
    print(f"{COLOR_BLUE}[INFO]{COLOR_RESET} {msg}")

def print_success(msg):
    print(f"{COLOR_GREEN}[SUCCESS]{COLOR_RESET} {msg}")

def print_warning(msg):
    print(f"{COLOR_YELLOW}[WARNING]{COLOR_RESET} {msg}")

def print_error(msg):
    print(f"{COLOR_RED}[ERROR]{COLOR_RESET} {msg}")
