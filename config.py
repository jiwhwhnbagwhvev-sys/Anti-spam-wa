# ==============================
# LOGIN DEFAULT
# ==============================
USERNAME = "Rio_V2-antispam"
PASSWORD = "Rio_V2-2026"

MAX_LOGIN_ATTEMPT = 3        # maksimal percobaan login
LOCK_TIME_SECONDS = 60       # waktu lock jika gagal login

# ==============================
# WARNA TERMINAL
# ==============================
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_BLUE = "\033[94m"
COLOR_YELLOW = "\033[93m"
COLOR_RESET = "\033[0m"

# ==============================
# LOADING SPINNER
# ==============================
SPINNER = ["|", "/", "-", "\\"]
LOADING_SPEED = 0.1

# ==============================
# ANTISPAM SETTINGS (opsional)
# ==============================
ANTI_SPAM_LOG = "spam_log.txt"    # file log spam
WHATSAPP_LOG = "whatsapp_log.txt" # log percobaan WA
DND_DEFAULT = True                 # default DND aktif
SILENCE_CALLS_DEFAULT = True       # default mute unknown calls
WHATSAPP_GUARD_DEFAULT = True      # default WA guard aktif
