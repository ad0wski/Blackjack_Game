import random

#ZASADY
zasady = """Witaj w Blackjacku!
Zasady gry:

Celem jest uzyskanie sumy kart jak najbliższej 21, ale jej nie przekroczyć.

Figury (J, Q, K) są warte 10 punktów, As może być za 1 lub 11.

Na początku dostajesz 2 karty, krupier również.

Możesz:

dobierać (hit), aby dostać nową kartę,

pasować (stand), aby zakończyć dobieranie.

Krupier dobiera karty, dopóki nie osiągnie co najmniej 17 punktów.

Wygrywa ten, kto jest bliżej 21, bez przekroczenia tej wartości.

Powodzenia! 🍀"""
# print(zasady)

taliaKart = {
    "♥️": ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"],
    "♦️": ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"],
    "♠️": ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"],
    "♣️": ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
}

wartosci = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11  # lub 1 w zależności od sytuacji
}


# zakladGracza = float(input("Za ile wchodzisz do gry? "))

znaki = ["♥️", "♦️", "♠️", "♣️"]
liczby = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

def dobierz_karte(znaki, liczby):
    losowyKolor = znaki[random.randint(0, 3)]
    losowaWartosc = liczby[random.randint(0, 12)]
    karta = losowaWartosc + losowyKolor
    return karta

kartyGracza = []
kartyKrupiera = []

#ROZDANIE KART
def rozdanieKartDlaGracza(kartyGracza):
    for i in range(2):
        wylosowanaKarta = dobierz_karte(znaki, liczby)
        kartyGracza.append(wylosowanaKarta)
    return kartyGracza

def rozdanieKartDlaKrupiera(kartyKrupiera):
    for i in range(2):
        wylosowanaKarta = dobierz_karte(znaki, liczby)
        kartyKrupiera.append(wylosowanaKarta)
    return kartyKrupiera

#ZLICZNIE PUNKTOW KART
def punktyGracza(kartyGracza, wartosci):
    punkty = 0
    for kartaGracza in kartyGracza:
        wartoscKarty = kartaGracza[:-2]
        punkty += wartosci[wartoscKarty]
    return punkty

print(punktyGracza(rozdanieKartDlaGracza(kartyGracza), wartosci))

def punktyKrupiera(kartyKrupiera, wartosci):
    punkty = 0
    for kartaKrupiera in kartyKrupiera:
        wartoscKarty = kartaKrupiera[:-2]
        punkty += wartosci[wartoscKarty]
    return punkty

print(punktyKrupiera(rozdanieKartDlaKrupiera(kartyGracza), wartosci))