#!/bin/bash
# NSec-Inyection by @nervius25


echo "----------------------------------------"
echo "[i] Installation NSec-Inyection"
echo "[i] We are now checking what system you are running."

if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "[i] Detected macOS."
    echo "[¡] Not compatible, only compatible with windows."

elif [ -f "/etc/debian_version" ] || [ -f "/etc/lsb-release" ]; then
    echo "[i] Detected Debian based Linux."
    echo "[¡] Not compatible, only compatible with windows."

elif [ -f "/etc/arch-release" ]; then 
    echo "[i] Detected Arch Linux."
    echo "[¡] Not compatible, only compatible with windows."
elif [[ "$OSTYPE" == "win32" || "$OS" == "Windows_NT" ]]; then
    echo "[i] Detected Windows."
    echo "[i] Installing on Windows..."
else
    echo "[¡] We could not detect your system."
    echo "[i] Please install some things manually."
    echo "[*] Only Compatible With WINDOWS."
    git clone https://github.com/nervius2525/NSec-Inyection.git > /dev/null 2>&1 || echo "[!] Please install git"
    cd NSec-Inyection
    python3 --help > /dev/null 2>&1 || echo "[!] Please install python3."
    pip3 install -r requirements.txt  > /dev/null 2>&1 || echo "[!] Could not install the requirements."
    python3 nsecinyection/main.py || echo "[!] Could not run NSec-Inyection."
fi

echo "[i] Done"
exit 0


# NSec-Inyection by @nervius25