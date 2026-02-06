import time
from adb_check import adb_shell, check_adb
from colors import print_info, print_success, print_error
from config import STATUS_DND

def enable_dnd():
    """
    Mengaktifkan Do Not Disturb (DND) Android
    """
    if not check_adb():
        print_error("Tidak bisa mengaktifkan DND: ADB tidak tersedia")
        return False

    try:
        adb_shell("settings put global zen_mode 1")  # 1 = DND total
        global STATUS_DND
        STATUS_DND = True
        print_success("DND berhasil diaktifkan!")
        return True
    except Exception as e:
        print_error(f"Gagal mengaktifkan DND: {e}")
        return False

def disable_dnd():
    """
    Menonaktifkan Do Not Disturb (DND) Android
    """
    if not check_adb():
        print_error("Tidak bisa menonaktifkan DND: ADB tidak tersedia")
        return False

    try:
        adb_shell("settings put global zen_mode 0")  # 0 = OFF
        global STATUS_DND
        STATUS_DND = False
        print_success("DND berhasil dinonaktifkan!")
        return True
    except Exception as e:
        print_error(f"Gagal menonaktifkan DND: {e}")
        return False

def toggle_dnd():
    """
    Toggle DND ON/OFF
    """
    if STATUS_DND:
        return disable_dnd()
    else:
        return enable_dnd()

def show_status():
    """
    Tampilkan status DND sekarang
    """
    status = "AKTIF" if STATUS_DND else "NONAKTIF"
    print_info(f"Status DND saat ini: {status}")

# ===== TEST REAL =====
if __name__ == "__main__":
    print_info("Menjalankan tes DND...")
    enable_dnd()
    time.sleep(2)
    show_status()
    time.sleep(2)
    disable_dnd()
    show_status()
