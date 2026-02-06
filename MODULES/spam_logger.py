import os
import time
from colors import print_info, print_success, print_error, COLOR_BLUE, COLOR_RESET
from config import LOG_SPAM_FILE, DEBUG_MODE

# ==============================
# LOGO TERMINATOR
# ==============================
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
        print(COLOR_BLUE + line + COLOR_RESET)
    print(COLOR_BLUE + "              SPAM LOGGER ACTIVE" + COLOR_RESET)
    print("="*60)
    print()

# ==============================
# Logging Fungsi
# ==============================
def log_spam(number, source="Unknown", type_spam="WA", status="Blocked"):
    """
    Catat spam ke file log
    """
    try:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        os.makedirs(os.path.dirname(LOG_SPAM_FILE), exist_ok=True)
        with open(LOG_SPAM_FILE, "a") as f:
            f.write(f"{timestamp} | {number} | {source} | {type_spam} | {status}\n")
        if DEBUG_MODE:
            print(f"[DEBUG] Log dibuat: {timestamp} | {number} | {source} | {type_spam} | {status}")
    except Exception as e:
        print_error(f"Gagal menulis log spam: {e}")

def view_logs(filter_type=None):
    """
    Tampilkan log spam, bisa filter berdasarkan tipe (WA/SMS/Call)
    """
    if not os.path.exists(LOG_SPAM_FILE):
        print_info("Belum ada log spam tersimpan")
        return

    print_info("Menampilkan log spam...")
    with open(LOG_SPAM_FILE, "r") as f:
        lines = f.readlines()
        for line in lines:
            if filter_type:
                if f"| {filter_type} |" in line:
                    print(line.strip())
            else:
                print(line.strip())

def search_number(number):
    """
    Cari log berdasarkan nomor
    """
    if not os.path.exists(LOG_SPAM_FILE):
        print_info("Belum ada log spam tersimpan")
        return

    found = False
    with open(LOG_SPAM_FILE, "r") as f:
        lines = f.readlines()
        for line in lines:
            if number in line:
                print(line.strip())
                found = True
    if not found:
        print_info(f"Tidak ada log untuk nomor: {number}")

# ==============================
# Test panjang & legal
# ==============================
if __name__ == "__main__":
    logo_terminator()
    print_info("Menjalankan Spam Logger Test Panjang...")
    
    # Simulasi log spam
    log_spam("+6281234567890", source="WA", type_spam="WA", status="Blocked")
    log_spam("+628111111111", source="SMS", type_spam="SMS", status="Blocked")
    log_spam("+628222222222", source="Call", type_spam="Call", status="Blocked")
    
    print_info("\nMenampilkan semua log spam:")
    view_logs()
    
    print_info("\nMenampilkan log spam WA saja:")
    view_logs(filter_type="WA")
    
    print_info("\nMencari log untuk nomor +628111111111:")
    search_number("+628111111111")
