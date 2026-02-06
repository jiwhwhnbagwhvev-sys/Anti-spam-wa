import time
from config import COLOR_BLUE, COLOR_RESET, SPINNER, LOADING_SPEED

def animate_banner():
    banner_lines = [
        "  █████╗ ███╗   ██╗████████╗██╗   ██╗███████╗    ███████╗██████╗ ███████╗",
        " ██╔══██╗████╗  ██║╚══██╔══╝██║   ██║██╔════╝    ██╔════╝██╔══██╗██╔════╝",
        " ███████║██╔██╗ ██║   ██║   ██║   ██║█████╗      █████╗  ██████╔╝█████╗  ",
        " ██╔══██║██║╚██╗██║   ██║   ██║   ██║██╔══╝      ██╔══╝  ██╔═══╝ ██╔══╝  ",
        " ██║  ██║██║ ╚████║   ██║   ╚██████╔╝███████╗    ███████╗██║     ███████╗",
        " ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚══════╝    ╚══════╝╚═╝     ╚══════╝",
        "                             ANTI SPAM REAL                                ",
        "                             v2.0-2026                                     ",
        "                       Developed by Rio_V2                                   "
    ]
    for line in banner_lines:
        print(COLOR_BLUE + line + COLOR_RESET)
        time.sleep(0.05)

def loading_animation(message="Sedang memuat"):
    import sys
    print()
    for i in range(10):
        for frame in SPINNER:
            sys.stdout.write(f"\r{COLOR_BLUE}{message} {frame}{COLOR_RESET}")
            sys.stdout.flush()
            time.sleep(LOADING_SPEED)
    print("\r" + COLOR_BLUE + message + " ✔" + COLOR_RESET + "          ")

def banner_full():
    animate_banner()
    loading_animation("Menyiapkan Anti-Spam...")
