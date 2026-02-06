# ================================
# CONFIG UTAMA ANTI-SPAM-REAL
# ================================

# ===== INFO APLIKASI =====
APP_NAME = "ANTI SPAM REAL"
APP_VERSION = "v2.0-2026"
APP_AUTHOR = "Rio_V2"

# ===== LOGIN (FIX SESUAI PERMINTAAN) =====
USERNAME = "Rio_V2-antispam"
PASSWORD = "Rio_V2-2026"

# ===== WARNA TERMINAL =====
COLOR_BLUE   = "\033[94m"
COLOR_GREEN  = "\033[92m"
COLOR_RED    = "\033[91m"
COLOR_YELLOW = "\033[93m"
COLOR_RESET  = "\033[0m"

# ===== MODE SISTEM =====
ANTI_SPAM_DEFAULT = True      # aktif otomatis
LOGGING_ENABLED   = True      # simpan bukti spam
ADB_REQUIRED      = True      # fitur nyata butuh ADB

# ===== PATH FOLDER =====
BASE_DIR   = "ANTI-SPAM-REAL"
LOG_DIR    = f"{BASE_DIR}/logs"
DATA_DIR   = f"{BASE_DIR}/data"
CORE_DIR   = f"{BASE_DIR}/core"

# ===== FILE DATA =====
SPAM_LOG_FILE      = f"{LOG_DIR}/spam.log"
BLACKLIST_FILE     = f"{DATA_DIR}/blacklist.txt"
WHITELIST_FILE     = f"{DATA_DIR}/whitelist.txt"
SESSION_FILE       = f"{DATA_DIR}/session.dat"

# ===== STATUS DEFAULT =====
STATUS_DND            = False
STATUS_SILENCE_CALLS  = False
STATUS_WHATSAPP_GUARD = False

# ===== PESAN STATUS =====
MSG_ON  = "AKTIF"
MSG_OFF = "NONAKTIF"

# ===== KEAMANAN =====
MAX_LOGIN_ATTEMPT = 3
LOCK_TIME_SECONDS = 30

# ===== ANIMASI =====
LOADING_SPEED = 0.2
SPINNER = ["|", "/", "-", "\\"]

# ===== DEBUG =====
DEBUG_MODE = False
