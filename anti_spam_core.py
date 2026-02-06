import time
from dnd_control import enable_dnd, disable_dnd, toggle_dnd, show_status as dnd_status
from silence_calls import enable_silence_calls, disable_silence_calls, toggle_silence_calls, show_status as silence_status
from whatsapp_guard import enable_whatsapp_guard, disable_whatsapp_guard, toggle_whatsapp_guard, show_status as wa_status, protect_single_target, protect_mass_targets, auto_detect_and_block
from spam_logger import log_spam, view_logs, search_number
from colors import print_info, print_success, print_error, print_warning, COLOR_BLUE, COLOR_RESET

# ==============================
# LOGO TERMINATOR CUSTOM
# ==============================
def logo_terminator():
    logo = [
        "████████╗██████╗ ██████╗ ███╗   ███╗ █████╗ ██████╗ ███████╗",
        "╚══██╔══╝██╔══██╗██╔══██╗████╗ ████║██╔══██╗██╔══██╗██╔════╝",
        "   ██║   ██████╔╝██████╔╝██╔████╔██║███████║██████╔╝█████╗  ",
        "   ██║   ██╔═══╝ ██╔═══╝ ██║╚██╔╝██║██╔══██║██╔═══╝ ██╔══╝  ",
        "   ██║   ██║     ██║     ██║ ╚═╝ ██║██║  ██║██║     ███████╗",
        "   ╚═╝   ╚═╝     ╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝",
        "                       ─── RIO_VIP2.0 ───"
    ]
    for line in logo:
        print(COLOR_BLUE + line.center(80) + COLOR_RESET)
    print(COLOR_BLUE + "="*80 + COLOR_RESET)
    print()

# ==============================
# ANTI-SPAM CORE
# ==============================

def single_target(number=None):
    """
    Proteksi single target: DND + Silence Calls + WhatsApp Guard + Logging
    """
    if not number:
        number = input("Masukkan nomor target: ").strip()
    print_info(f"Memproses proteksi untuk nomor: {number}...")
    
    enable_dnd()
    enable_silence_calls()
    enable_whatsapp_guard()
    
    protect_single_target(number)
    log_spam(number, source="All", type_spam="Mixed", status="Blocked")
    
    print_success(f"Proteksi single target untuk {number} selesai!")
    input("Tekan Enter untuk kembali...")

def mass_target(numbers=None):
    """
    Proteksi massal target
    """
    if not numbers:
        numbers_input = input("Masukkan nomor target dipisah koma (,): ")
        numbers = [n.strip() for n in numbers_input.split(",") if n.strip()]
    
    print_info("Memproses proteksi massal...")
    enable_dnd()
    enable_silence_calls()
    enable_whatsapp_guard()
    
    protect_mass_targets(numbers)
    for num in numbers:
        log_spam(num, source="All", type_spam="Mixed", status="Blocked")
    
    print_success("Proteksi massal selesai!")
    input("Tekan Enter untuk kembali...")

def view_targets():
    """
    Menu lihat target spam / log spam
    """
    while True:
        print_info("\nMenu Lihat Target Spam")
        print(f"{COLOR_BLUE}1. Lihat semua log{COLOR_RESET}")
        print(f"{COLOR_BLUE}2. Filter log per tipe (WA/SMS/Call){COLOR_RESET}")
        print(f"{COLOR_BLUE}3. Cari nomor tertentu{COLOR_RESET}")
        print(f"{COLOR_BLUE}4. Kembali{COLOR_RESET}")
        choice = input("Pilih menu: ").strip()
        
        if choice == "1":
            view_logs()
        elif choice == "2":
            tipe = input("Masukkan tipe (WA/SMS/Call): ").strip()
            view_logs(filter_type=tipe)
        elif choice == "3":
            nomor = input("Masukkan nomor: ").strip()
            search_number(nomor)
        elif choice == "4":
            break
        else:
            print_warning("Pilihan tidak valid!")
        input("Tekan Enter untuk lanjut...")

def full_protection_test():
    """
    Jalankan semua proteksi sekaligus (test panjang & legal)
    """
    logo_terminator()
    print_info("Menjalankan full Anti-Spam protection test...")
    enable_dnd()
    enable_silence_calls()
    enable_whatsapp_guard()
    
    test_numbers = ["+6281234567890", "+628111111111", "+628222222222", "+628333333333"]
    print_info("Proteksi massal untuk test numbers...")
    protect_mass_targets(test_numbers)
    auto_detect_and_block([{"number": n, "spam": True} for n in test_numbers])
    for n in test_numbers:
        log_spam(n, source="All", type_spam="Mixed", status="Blocked")
    
    dnd_status()
    silence_status()
    wa_status()
    print_success("Full Anti-Spam protection test selesai!")

# ==============================
# TEST CORE
# ==============================
if __name__ == "__main__":
    logo_terminator()
    print_info("Menjalankan Anti-Spam Core Test Panjang...")
    single_target()
    mass_target()
    view_targets()
    full_protection_test()
