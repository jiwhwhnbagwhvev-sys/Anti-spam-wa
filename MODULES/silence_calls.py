from adb_check import adb_shell, check_adb
from colors import print_info, print_success, print_error
from config import STATUS_SILENCE_CALLS

def enable_silence_calls():
    """
    Mengaktifkan Silence Unknown Calls Android
    """
    if not check_adb():
        print_error("Tidak bisa mengaktifkan Silence Calls: ADB tidak tersedia")
        return False

    try:
        # 1 = menyenyapkan panggilan dari nomor asing
        adb_shell("settings put secure silence_unknown_callers 1")
        global STATUS_SILENCE_CALLS
        STATUS_SILENCE_CALLS = True
        print_success("Silence Unknown Calls berhasil diaktifkan!")
        return True
    except Exception as e:
        print_error(f"Gagal mengaktifkan Silence Calls: {e}")
        return False

def disable_silence_calls():
    """
    Menonaktifkan Silence Unknown Calls Android
    """
    if not check_adb():
        print_error("Tidak bisa menonaktifkan Silence Calls: ADB tidak tersedia")
        return False

    try:
        adb_shell("settings put secure silence_unknown_callers 0")
        global STATUS_SILENCE_CALLS
        STATUS_SILENCE_CALLS = False
        print_success("Silence Unknown Calls berhasil dinonaktifkan!")
        return True
    except Exception as e:
        print_error(f"Gagal menonaktifkan Silence Calls: {e}")
        return False

def toggle_silence_calls():
    """
    Toggle Silence Unknown Calls ON/OFF
    """
    if STATUS_SILENCE_CALLS:
        return disable_silence_calls()
    else:
        return enable_silence_calls()

def show_status():
    """
    Tampilkan status Silence Unknown Calls sekarang
    """
    status = "AKTIF" if STATUS_SILENCE_CALLS else "NONAKTIF"
    print_info(f"Status Silence Unknown Calls: {status}")

# ===== TEST REAL =====
if __name__ == "__main__":
    print_info("Menjalankan tes Silence Calls...")
    enable_silence_calls()
    show_status()
    disable_silence_calls()
    show_status()
