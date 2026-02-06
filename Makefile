cd ~/Anti-spam-wa
cat > Makefile << 'EOF'
# ==============================
# Makefile untuk Anti-Spam-Termux
# ==============================

.PHONY: run install

install:
	bash SH/install.sh

run:
	./run.sh
EOF
