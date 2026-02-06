#!/data/data/com.termux/files/usr/bin/bash

# ==============================
# ANTI SPAM TERMINATOR - INSTALLER
# ==============================
# Installer ini:
# - Update paket Termux
# - Install dependency (python, adb-tools)
# - Buat struktur folder rapi
# - Set permission
# - Buat script run cepat
# ==============================

set -e

BLUE="\033[94m"
GREEN="\033[92m"
RED="\033[91m"
YELLOW="\033[93m"
RESET="\033[0m"

BASE_DIR="$HOME/ANTI-SPAM-REAL"
PY_DIR="$BASE_DIR/PY_FILES"
MOD_DIR="$BASE_DIR/MODULES"
SH_DIR="$BASE_DIR/SH"
LOG_DIR="$BASE_DIR/logs"

print_info()   { echo -e "${BLUE}[INFO]${RESET} $1"; }
print_ok()     { echo -e "${GREEN}[OK]${RESET} $1"; }
print_warn()   { echo -e "${YELLOW}[WARN]${RESET} $1"; }
print_err()    { echo -e "${RED}[ERR]${RESET} $1"; }

clear
echo -e "${BLUE}"
echo "████████╗██████╗ ██████╗ ███╗   ███╗ █████╗ ██████╗ ███████╗"
echo "╚══██╔══╝██╔══██╗██╔══██╗████╗ ████║██╔══██╗██╔══██╗██╔════╝"
echo "   ██║   ██████╔╝██████╔╝██╔████╔██║███████║██████╔╝█████╗  "
echo "   ██║   ██╔═══╝ ██╔═══╝ ██║╚██╔╝██║██╔══██║██╔═══╝ ██╔══╝  "
echo "   ██║   ██║     ██║     ██║ ╚═╝ ██║██║  ██║██║     ███████╗"
echo "   ╚═╝   ╚═╝     ╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝"
echo -e "${RESET}"
echo "ANTI SPAM TERMINATOR - INSTALLER"
echo "============================================================"
sleep 1

# ==============================
# Update & Upgrade
# ==============================
print_info "Update paket Termux..."
pkg update -y && pkg upgrade -y
print_ok "Update selesai"

# ==============================
# Dependency
# ==============================
print_info "Install dependency..."
pkg install -y python adb-tools coreutils
print_ok "Dependency terpasang"

# ==============================
# Storage Permission
# ==============================
print_info "Meminta akses storage..."
termux-setup-storage || true
print_ok "Akses storage siap"

# ==============================
# Folder Structure
# ==============================
print_info "Membuat struktur folder..."
mkdir -p "$PY_DIR" "$MOD_DIR" "$SH_DIR" "$LOG_DIR"
print_ok "Folder dibuat"

# ==============================
# Permission
# ==============================
print_info "Set permission script..."
chmod +x "$SH_DIR"/*.sh 2>/dev/null || true
print_ok "Permission diset"

# ==============================
# Run Shortcut
# ==============================
RUN_SCRIPT="$BASE_DIR/run.sh"
print_info "Membuat run shortcut..."
cat > "$RUN_SCRIPT" << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
cd "$HOME/ANTI-SPAM-REAL" || exit 1
python PY_FILES/main.py
EOF
chmod +x "$RUN_SCRIPT"
print_ok "Shortcut dibuat: $RUN_SCRIPT"

# ==============================
# ADB Check
# ==============================
print_info "Cek ADB..."
if command -v adb >/dev/null 2>&1; then
  print_ok "ADB tersedia"
  print_warn "Pastikan USB Debugging aktif di HP target (Settings > Developer options)"
else
  print_warn "ADB belum terdeteksi, beberapa fitur tidak aktif"
fi

# ==============================
# Finish
# ==============================
echo
print_ok "INSTALL SELESAI"
echo "Cara menjalankan:"
echo "  cd ~/ANTI-SPAM-REAL"
echo "  ./run.sh"
echo
print_warn "Catatan:"
echo "- Fitur memanfaatkan pengaturan sistem yang tersedia (DND, silence calls, notifikasi)."
echo "- Tidak melakukan peretasan jaringan/operator."
echo "============================================================"
