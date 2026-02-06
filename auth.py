import os
import time
import hashlib
import pickle
from config import SESSION_FILE, COLOR_GREEN, COLOR_RED, COLOR_YELLOW, COLOR_RESET, DEBUG_MODE
from colors import print_info, print_success, print_error, print_debug

# ===== CEK / BUAT SESSION =====
def create_session(username):
    try:
        with open(SESSION_FILE, "wb") as f:
            data = {
                "username": username,
                "login_time": time.time()
            }
            pickle.dump(data, f)
        print_success("Session berhasil dibuat.")
    except Exception as e:
        print_error(f"Gagal membuat session: {e}")

def load_session():
    if not os.path.exists(SESSION_FILE):
        return None
    try:
        with open(SESSION_FILE, "rb") as f:
            data = pickle.load(f)
            return data
    except Exception as e:
        print_error(f"Gagal memuat session: {e}")
        return None

def clear_session():
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
        print_info("Session dihapus.")

# ===== LOGIN VALIDATION & HASHING =====
def hash_password(password):
    """Hash password menggunakan SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_session(username):
    session = load_session()
    if session and session.get("username") == username:
        print_success(f"Session aktif untuk user: {username}")
        return True
    return False

# ===== DEBUG =====
if DEBUG_MODE:
    print_debug("Auth module loaded")
