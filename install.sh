#!/data/data/com.termux/files/usr/bin/bash

clear
echo -e "\033[34m"
echo "======================================"
echo "        ANTI SPAM REAL INSTALLER       "
echo "======================================"
echo -e "\033[0m"

sleep 1

echo "[+] Mengecek Termux..."
if [ ! -d "$PREFIX" ]; then
    echo "[!] Termux tidak terdeteksi!"
    exit 1
fi
echo "[✓] Termux OK"

sleep 1
echo
echo "[+] Update package..."
pkg update -y && pkg upgrade -y

sleep 1
echo
echo "[+] Install dependency utama..."
pkg install -y python android-tools git nano

sleep 1
echo
echo "[+] Mengecek Python..."
python --version
if [ $? -ne 0 ]; then
    echo "[!] Python gagal terinstall"
    exit 1
fi
echo "[✓] Python siap"

sleep 1
echo
echo "[+] Mengecek ADB..."
adb version
if [ $? -ne 0 ]; then
    echo "[!] ADB tidak tersedia"
    exit 1
fi
echo "[✓] ADB siap"

sleep 1
echo
echo "[+] Meminta izin storage..."
termux-setup-storage

sleep 2
echo
echo "[+] Membuat struktur folder project..."

mkdir -p ANTI-SPAM-REAL/logs
mkdir -p ANTI-SPAM-REAL/data
mkdir -p ANTI-SPAM-REAL/core

sleep 1
echo "[✓] Folder dibuat"

sleep 1
echo
echo "[+] Memberi permission file..."
chmod +x *.py 2>/dev/null

sleep 1
echo
echo "======================================"
echo " INSTALL SELESAI"
echo "======================================"
echo
echo "LANGKAH SELANJUTNYA:"
echo "1. Aktifkan Developer Options di HP"
echo "2. Aktifkan USB Debugging / Wireless Debugging"
echo "3. Jalankan: python main.py"
echo
echo -e "\033[32mANTI-SPAM-REAL siap digunakan\033[0m"
