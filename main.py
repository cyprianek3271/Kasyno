import time
import random
import os
from colorama import Fore, Style, init
import math




init(autoreset=True)

def pisz(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
def konfetti():
    kolory = [Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.MAGENTA]
    for _ in range(10):
        print(random.choice(kolory) + "💸 " * random.randint(5, 10))
        time.sleep(0.05)
    print(Style.RESET_ALL)
def czysc():
    os.system('cls' if os.name == 'nt' else 'clear')
def pokaz_kasyno():
    czysc()
    for i in range(20):  # miga napis CASINO 3 razy
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
        |  │ []  []  []  []  []  []  []   │  |
        |  │ []  []  []  []  []  []  []   │  |
        |  │ []  []  []  []  []  []  []   │  |
        |  │ []  []  []  []  []  []  []   │  |
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
        czysc()
        print(kasyno)
        time.sleep(0.2)
    print(pisz('Witamy w naszym kasynie!'))
    time.sleep(1)



RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
BOLD = "\033[1m"

# ASCII kostka
KOSTKA = {
    1: ["╔═════╗", "║     ║", "║  ●  ║", "║     ║", "╚═════╝"],
    2: ["╔═════╗", "║ ●   ║", "║     ║", "║   ● ║", "╚═════╝"],
    3: ["╔═════╗", "║ ●   ║", "║  ●  ║", "║   ● ║", "╚═════╝"],
    4: ["╔═════╗", "║ ● ● ║", "║     ║", "║ ● ● ║", "╚═════╝"],
    5: ["╔═════╗", "║ ● ● ║", "║  ●  ║", "║ ● ● ║", "╚═════╝"],
    6: ["╔═════╗", "║ ● ● ║", "║ ● ● ║", "║ ● ● ║", "╚═════╝"],
}

def czysc():
    os.system("cls" if os.name == "nt" else "clear")

def pokaz_kostke(n):
    for linia in KOSTKA[n]:
        print(f"{YELLOW}{BOLD}{linia}{RESET}")
    print()

def animacja_kostki():
    for _ in range(8):
        n = random.randint(1, 6)
        czysc()
        print(f"{CYAN}{BOLD}Rzucasz kostką... 🎲{RESET}\n")
        pokaz_kostke(n)
        time.sleep(0.1)
    wynik = random.randint(1, 6)
    czysc()
    print(f"{GREEN}{BOLD}Kostka zatrzymała się! Wynik:{RESET} {YELLOW}{wynik}{RESET}\n")
    pokaz_kostke(wynik)
    time.sleep(1)
    return wynik

def Kosci(stawka):
    global pieniadze
    czysc()
    print(Fore.CYAN + BOLD + "\n🎲 Witaj w DICE DUEL! 🎲" + Style.RESET_ALL)
    print("Masz 3 próby. Każdy rzut zwiększa mnożnik — ale jeśli wypadnie 1, tracisz wszystko z tej rundy.")
    print(Fore.YELLOW + f"\nWchodzisz do gry za {stawka}$ — kasa zostaje w kasynie! 💸" + Style.RESET_ALL)
    input("\nNaciśnij Enter, aby rozpocząć...")
    pieniadze -= stawka

    rundy = 3
    suma_wygranej = 0

    for runda in range(1, rundy + 1):
        czysc()
        print(Fore.YELLOW + f"🔥 Runda {runda}/{rundy} 🔥" + Style.RESET_ALL)
        input("Naciśnij Enter, aby rzucić kostką...")

        mnoznik = 1.0
        runda_trwa = True
        runda_wygrana = 0

        while runda_trwa:
            rzut = animacja_kostki()

            if rzut == 1:
                print(Fore.RED + "💀 Wypadło 1! Tracisz wszystko z tej rundy." + Style.RESET_ALL)
                runda_wygrana = 0
                time.sleep(1.5)
                break
            else:
                mnoznik *= 1.2  # trochę wyższy mnożnik — więcej ryzyka, więcej zysku!
                runda_wygrana = int((stawka / 2.3) * (mnoznik - 1))
                print(f"{Fore.GREEN}✅ Dobry rzut! Mnożnik teraz: ×{mnoznik:.2f}{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Potencjalna wygrana tej rundy: {runda_wygrana}${Style.RESET_ALL}")
                decyzja = input("Rzucasz dalej? (t/n): ").strip().lower()
                if decyzja != 't':
                    break

        suma_wygranej += runda_wygrana
        print(f"\n💰 Z tej rundy zdobywasz: {Fore.GREEN}{runda_wygrana}${Style.RESET_ALL}")
        time.sleep(1.8)

    czysc()
    print(Fore.CYAN + "🎯 KONIEC GRY 🎯" + Style.RESET_ALL)
    if suma_wygranej > 0:
        pieniadze += suma_wygranej
        print(f"{Fore.GREEN}Wygrałeś razem: {suma_wygranej}$!{Style.RESET_ALL}")
        konfetti()
    else:
        print(f"{Fore.RED}Niestety, tym razem bez wygranej...{Style.RESET_ALL}")

    print(f"💵 Twój aktualny balans: {Fore.CYAN}{pieniadze}${Style.RESET_ALL}")
    time.sleep(3)





# ===========================
# 🃏 BLACKJACK
# ===========================
Black_Jack_lista = {
    'As': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'Walet': 10, 'Dama': 10, 'Król': 10
}

def Black_Jack(stawka):
    global pieniadze
    pieniadze -= stawka
    czysc()
    print(Fore.YELLOW + "\nWitaj w Black Jack! 🃏 Zacznijmy grę.\n" + Style.RESET_ALL)

    talia = list(Black_Jack_lista.keys()) * 4
    random.shuffle(talia)
    
    gracz_karty = []
    bot_karty = []

    def rozdaj_karty(ilosc, gracz, bot):
        for _ in range(ilosc):
            if gracz == 't':
                gracz_karty.append(talia.pop())
            if bot == 't':
                bot_karty.append(talia.pop())

    def oblicz_wartosc(karty):
        wartosc = sum(Black_Jack_lista[karta] for karta in karty)
        asy = karty.count('As')
        while wartosc > 21 and asy:
            wartosc -= 10
            asy -= 1
        return wartosc

    # Rozdanie startowych kart
    rozdaj_karty(2, 't', 't')
    print(f"Twoje karty: {Fore.CYAN}{gracz_karty}{Style.RESET_ALL}, Wartość: {oblicz_wartosc(gracz_karty)}")

    # Tura gracza
    while True:
        if oblicz_wartosc(gracz_karty) > 21:
            print(Fore.RED + "Przekroczyłeś 21!" + Style.RESET_ALL)
            break
        warunek = input("Czy dobierasz kartę? (t/n): ").strip().lower()
        if warunek == 't':
            rozdaj_karty(1, 't', 'n')
            print(f"Twoje karty: {Fore.CYAN}{gracz_karty}{Style.RESET_ALL}, Wartość: {oblicz_wartosc(gracz_karty)}")
        else:
            break

    # Tura bota
    while oblicz_wartosc(bot_karty) <= 11:
        rozdaj_karty(1, 'n', 't')

    gracz_wartosc = oblicz_wartosc(gracz_karty)
    bot_wartosc = oblicz_wartosc(bot_karty)
    print(f"\nTwoje karty: {Fore.CYAN}{gracz_karty}{Style.RESET_ALL} = {gracz_wartosc}")
    print(f"Karty bota: {Fore.MAGENTA}{bot_karty}{Style.RESET_ALL} = {bot_wartosc}")



    # Wynik
    if gracz_wartosc > 21:
        print(Fore.RED + f"Przegrałeś! Tracisz {stawka}" + Style.RESET_ALL)
        
    elif gracz_wartosc > bot_wartosc or bot_wartosc > 21:
        losowosc = random.uniform(1.3, 2.1)
        suma = math.floor(losowosc* stawka)
        print(Fore.GREEN + f"Wygrałeś! Dostajesz {suma})" + Style.RESET_ALL)
        pieniadze += suma
        konfetti()
    elif gracz_wartosc < bot_wartosc:
        print(Fore.RED + f"Przegrałeś! Tracisz {stawka}" + Style.RESET_ALL)
        
    else:
        print(Fore.YELLOW + "Remis! Stawka wraca do Ciebie." + Style.RESET_ALL)
        pieniadze += stawka
    print(f"\n💰 Twój balans: {Fore.CYAN}{pieniadze}{Style.RESET_ALL}\n")
    time.sleep(2)

# ===========================
# 🎡 RULETKA
# ===========================
def ruleta(stawka):
    global pieniadze
    pieniadze -= stawka
    def krec_kolem():
        kolory = ['Czarny'] * 10 + ['Czerwony'] * 10 + ['Zielony']
        print(Fore.YELLOW + "Kręcimy ruletkę..." + Style.RESET_ALL)
        czas = 0.05
        for _ in range(30):
            i = random.randint(0, len(kolory)-1)
            kolor = kolory[i]
            kol = Fore.RED if kolor == 'Czerwony' else (Fore.GREEN if kolor == 'Zielony' else Fore.WHITE)
            print(f"\r{kol}[ {kolor} ]", end="")
            time.sleep(czas)
            czas += 0.03
        print("\n")
        wynik = random.choice(kolory)
        print(f"🎯 Koło zatrzymało się na: {Fore.GREEN if wynik=='Zielony' else (Fore.RED if wynik=='Czerwony' else Fore.WHITE)}{wynik}{Style.RESET_ALL}\n")
        return wynik

    stawiam = input("Na jaki kolor stawiasz? (czerwony/czarny/zielony): ").strip().lower()
    wynik = krec_kolem()

    if wynik.lower() == stawiam:
        if wynik == 'Zielony':
            pieniadze += stawka * 7
            print(Fore.GREEN + f"Trafiłeś zielone! Wygrywasz {stawka*7} 💸" + Style.RESET_ALL)
        else:
            pieniadze += stawka * 2
            print(Fore.GREEN + f"Trafiłeś! Wygrywasz {stawka*2} 💰" + Style.RESET_ALL)
            konfetti()
    else:
        
        print(Fore.RED + f"Przegrałeś! Tracisz {stawka} 💸" + Style.RESET_ALL)

    print(f"Twój aktualny balans: {Fore.CYAN}{pieniadze}{Style.RESET_ALL}\n")
    time.sleep(2)
# ===========================
# 🎡 RULETKA
# ===========================
def skrzynki(stawka):
    global pieniadze
    pieniadze -= stawka

    def kartony_obok(ile):
        karton = [
            "    _________    ",
            "   /        /|   ",
            "  /________/ |   ",
            "  |        | |   ",
            "  |  BOX   | /   ",
            "  |________|/    "
        ]
        for linia in karton:
            wiersz = ""
            for _ in range(ile):
                wiersz += linia + "  "
            print(wiersz)

    kartony_obok(4)

    # Słownik z początkowymi wartościami
    kartony = {'k1': 0, 'k2': 0, 'k3': 0, 'k4': 0}

    # Losowa kolejność kluczy
    klucze = list(kartony.keys())
    random.shuffle(klucze)

    mnoznik = 0.5
    for key in klucze:
        kartony[key] = mnoznik
        mnoznik += 0.5

    print(kartony)


    

    
# ===========================
# 🎮 Główna pętla gry
# ===========================
pieniadze = 1000
Gra = True

pokaz_kasyno()

while Gra:
    if pieniadze == 0:
        czysc()
        pisz('Zbankrutowałeś', 0.02)
        pisz('Koniec gry', 0.02)
        break
    czysc()
    print(Fore.YELLOW + f"💰 Twój balans: {pieniadze}" + Style.RESET_ALL)
    wybor = input("Na jaką maszynę idziesz? Black Jack: (B), Ruletka: (R), Kości (K) Wyjście: (Q): ").strip().lower()

    if wybor == 'b':
        stawka = input("Podaj stawkę: ").strip().lower()
        if stawka == 'all':
            stawka = pieniadze
        stawka = int(stawka)
        pieniadze = int(pieniadze)
        if stawka > pieniadze:
            print(Fore.RED + "Nie masz wystarczająco pieniędzy!" + Style.RESET_ALL)
            time.sleep(1.5)
            continue
        Black_Jack(stawka)
        

            


    elif wybor == 'r':
        stawka = input("Podaj stawkę: ").strip().lower()
        if stawka == 'all':
            stawka = pieniadze
        stawka = int(stawka)
        pieniadze = int(pieniadze)
        if stawka > pieniadze:
            print(Fore.RED + "Nie masz wystarczająco pieniędzy!" + Style.RESET_ALL)
            time.sleep(1.5)
            continue
        ruleta(stawka)

    elif wybor == 'p':
        stawka = input("Podaj stawkę: ").strip().lower()
        if stawka == 'all':
            stawka = pieniadze
        stawka = int(stawka)
        pieniadze = int(pieniadze)
        if stawka > pieniadze:
            print(Fore.RED + "Nie masz wystarczająco pieniędzy!" + Style.RESET_ALL)
            time.sleep(1.5)
            continue
        skrzynki(stawka)

    elif wybor == 'k':
        stawka = input("Podaj stawkę: ").strip().lower()
        if stawka == 'all':
            stawka = pieniadze
        stawka = int(stawka)
        pieniadze = int(pieniadze)
        if stawka > pieniadze:
            print(Fore.RED + "Nie masz wystarczająco pieniędzy!" + Style.RESET_ALL)
            time.sleep(1.5)
            continue
        Kosci(stawka)

    elif wybor == 'q':
        print(Fore.CYAN + "Dzięki za grę! 👋" + Style.RESET_ALL)
        Gra = False

    else:
        print(Fore.RED + "Niepoprawny wybór!" + Style.RESET_ALL)
        time.sleep(1.5)
