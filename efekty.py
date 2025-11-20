import os
import time
import random
from colorama import Fore, Style, init

init(autoreset=True)

# ===========================
# 🧹 Czyszczenie ekranu
# ===========================
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ===========================
# ✍️ Efekt pisania (animowany tekst)
# ===========================
def pisz(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# ===========================
# 🎉 Efekt konfetti przy wygranej
# ===========================
def konfetti():
    kolory = [Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.MAGENTA]
    for _ in range(15):
        print(random.choice(kolory) + "💸 " * random.randint(5, 10))
        time.sleep(0.05)
    print(Style.RESET_ALL)

# ===========================
# 💰 Pasek statusu u góry ekranu
# ===========================
def pasek_statusu(pieniadze, gracz="Gracz"):
    print(Fore.YELLOW + "═" * 60)
    print(
        f"{Fore.CYAN}🎰 KASYN0 ROYALE  {Fore.YELLOW}|  "
        f"{Fore.GREEN}💰 Balans: {pieniadze}  {Fore.YELLOW}|  "
        f"{Fore.MAGENTA}👤 {gracz}"
    )
    print(Fore.YELLOW + "═" * 60 + Style.RESET_ALL)

# ===========================
# 🎰 Logo kasyna z animacją
# ===========================
def pokaz_kasyno():
    clear()
    for i in range(3):
        kasyno = f"""{Fore.YELLOW}
             ____________________________
            /                            \\
           /   ████████████████████████   \\
          /   █   █   █   █   █   █   █    \\
         /    █   █   █   █   █   █   █     \\
        /____________________________________\\
        |                                    |
        |    ╔══════════════════════════╗    |
        |    ║         {Fore.RED if i % 2 == 0 else Fore.YELLOW}CASINO 🎰{Fore.YELLOW}        ║    |
        |    ╚══════════════════════════╝    |
        |  ┌──────────────────────────────┐  |
        |  │ []  []  []  []  []  []  []  │  |
        |  │ []  []  []  []  []  []  []  │  |
        |  │ []  []  []  []  []  []  []  │  |
        |  │ []  []  []  []  []  []  []  │  |
        |  └──────────────────────────────┘  |
        |          ____      ____            |
        |         |    |    |    |           |
        |         |DOOR|    |DOOR|           |
        |         |____|    |____|           |
        |____________________________________|
                 |                    |
                 |____________________|
                 /====================\\
                /______________________\\
{Style.RESET_ALL}"""
        clear()
        print(kasyno)
        time.sleep(0.5)
    pisz(Fore.CYAN + "\nWitamy w naszym wirtualnym kasynie! 💸" + Style.RESET_ALL, 0.02)
    time.sleep(1.5)
    clear()
