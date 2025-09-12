import random

#ZASADY
zasady = """\nWitaj w Blackjacku!
Zasady gry:

Celem jest uzyskanie sumy kart jak najbliższej 21, ale jej nie przekroczyć.

Figury (J, Q, K) są warte 10 punktów, As może być za 1 lub 11.

Na początku dostajesz 2 karty, krupier również.

Możesz:

dobierać (hit), aby dostać nową kartę,

pasować (stand), aby zakończyć dobieranie.

Krupier dobiera karty, dopóki nie osiągnie co najmniej 17 punktów.

Wygrywa ten, kto jest bliżej 21, bez przekroczenia tej wartości.

Powodzenia! 🍀\n"""

# print(zasady)

wartosci = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11  # lub 1 w zależności od sytuacji
}

# znaki = ["♥️", "♦️", "♠️", "♣️"]
# liczby = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# def dobierz_karte(znaki, liczby):
#     losowyKolor = znaki[random.randint(0, 3)]
#     losowaWartosc = liczby[random.randint(0, 12)]
#     karta = losowaWartosc + losowyKolor
#     return karta

kartyGracza = []
kartyKrupiera = []

dostepneKartyWTalii = ["2♥️", "3♥️", "4♥️", "5♥️", "6♥️", "7♥️", "8♥️", "9♥️", "10♥️", "J♥️", "Q♥️", "K♥️", "A♥️", 
                       "2♦️", "3♦️", "4♦️", "5♦️", "6♦️", "7♦️", "8♦️", "9♦️", "10♦️", "J♦️", "Q♦️", "K♦️", "A♦️",
                       "2♠️", "3♠️", "4♠️", "5♠️", "6♠️", "7♠️", "8♠️", "9♠️", "10♠️", "J♠️", "Q♠️", "K♠️", "A♠️",
                       "2♣️", "3♣️", "4♣️", "5♣️", "6♣️", "7♣️", "8♣️", "9♣️", "10♣️", "J♣️", "Q♣️", "K♣️", "A♣️"]


#ROZDANIE KART
def rozdanieKartDlaGracza(kartyGracza, dostepneKartyWTalii):
    for i in range(2):
        wylosowanaKarta = dostepneKartyWTalii[random.randint(0, len(dostepneKartyWTalii) - 1)]
        kartyGracza.append(wylosowanaKarta)
        dostepneKartyWTalii.remove(wylosowanaKarta)
    return kartyGracza

def rozdanieKartDlaKrupiera(kartyKrupiera, dostepneKartyWTalii):
    for i in range(2):
        wylosowanaKarta = dostepneKartyWTalii[random.randint(0, len(dostepneKartyWTalii) - 1)]
        kartyKrupiera.append(wylosowanaKarta)
        dostepneKartyWTalii.remove(wylosowanaKarta)
    return kartyKrupiera


#ZLICZNIE PUNKTOW KART
def punktyGracza(kartyGracza, wartosci):
    punkty = 0
    for kartaGracza in kartyGracza:
        wartoscKarty = kartaGracza[:-2]
        punkty += wartosci[wartoscKarty]
    return punkty


def punktyKrupiera(kartyKrupiera, wartosci):
    punkty = 0
    for kartaKrupiera in kartyKrupiera:
        wartoscKarty = kartaKrupiera[:-2]
        punkty += wartosci[wartoscKarty]
    return punkty

rozdanieKartDlaGracza(kartyGracza, dostepneKartyWTalii)
rozdanieKartDlaKrupiera(kartyKrupiera, dostepneKartyWTalii)

print("Karty gracza:", kartyGracza, "=> punkty:", punktyGracza(kartyGracza, wartosci))
print("Karty krupiera:", [kartyKrupiera[0], "??"], "punkty:", punktyKrupiera([kartyKrupiera[0]], wartosci)) # tylko 1 karta widoczna


#DOBIERANIE KART PRZEZ GRACZA
czyGraczPrzegral = False
while True:
    decyzja = input("Dobierasz kartę (h) czy pasujesz (s)? ")
    if decyzja == "h":
        wylosowanaKarta = dostepneKartyWTalii[random.randint(0, len(dostepneKartyWTalii) - 1)]
        kartyGracza.append(wylosowanaKarta)
        dostepneKartyWTalii.remove(wylosowanaKarta)
        print("Karty gracza:", kartyGracza, "=> punkty:", punktyGracza(kartyGracza, wartosci))
        if punktyGracza(kartyGracza, wartosci) == 21:
            break
        elif punktyGracza(kartyGracza, wartosci) > 21:
            print("Krupier wygrywa! (gracz bust)")
            czyGraczPrzegral = True
            break
        else:
            continue
    elif decyzja == "s":
        print("Spasowales! Teraz kolej krupiera. ")
        break
    else:
        print("Blad! Wpisz 'h' albo 's'. ")


# def sprawdzWyniki(gracz, krupier):
#     if gracz > 21:
#         return "Krupier wygrywa! (gracz bust)"
#     elif krupier > 21:
#         return "Gracz wygrywa! (krupier bust)"
#     elif gracz > krupier:
#         return "Gracz wygrywa!"
#     elif krupier > gracz:
#         return "Krupier wygrywa!"
#     else:
#         return "Remis!"


# DOBIERANIE KART PRZEZ KRUPIERA
punktyKartKrupiera = punktyKrupiera(kartyKrupiera, wartosci)
if czyGraczPrzegral == False:
    while True:
        print("Karty krupiera:", kartyKrupiera, "punkty:", punktyKrupiera(kartyKrupiera, wartosci))
        if punktyKrupiera(kartyKrupiera, wartosci) < 17:
            wylosowanaKarta = dostepneKartyWTalii[random.randint(0, len(dostepneKartyWTalii) - 1)]
            kartyKrupiera.append(wylosowanaKarta)
            dostepneKartyWTalii.remove(wylosowanaKarta)
            print("Karty krupiera:", kartyKrupiera, "=> punkty:", punktyKrupiera(kartyKrupiera, wartosci))
            if punktyKrupiera(kartyKrupiera, wartosci) > 21:
                print("Gracz wygrywa! (krupier bust) ")
                wygranaGracza = True
                break
            elif punktyKrupiera(kartyKrupiera, wartosci) == 21 and punktyGracza(kartyGracza, wartosci) == 21:
                print("Remis! ")
                break
            elif punktyKrupiera(kartyKrupiera, wartosci) >= 17 and punktyKrupiera(kartyKrupiera, wartosci) < 21:
                if punktyKrupiera(kartyKrupiera, wartosci) < punktyGracza(kartyGracza, wartosci):
                    wygranaGracza = True
                    print("Gracz wygrywa! ")
                    break
                elif punktyKrupiera(kartyKrupiera, wartosci) > punktyGracza(kartyGracza, wartosci):
                    wygranaKrupiera = True
                    print("Krupier wygrywa! ")
                    break
                elif punktyKrupiera(kartyKrupiera, wartosci) == punktyGracza(kartyGracza, wartosci):
                    print("Remis! ")
                    break
            else:
                continue
        else:
            if punktyKrupiera(kartyKrupiera, wartosci) < punktyGracza(kartyGracza, wartosci):
                wygranaGracza = True
                print("Gracz wygrywa! ")
                break
            elif punktyKrupiera(kartyKrupiera, wartosci) > punktyGracza(kartyGracza, wartosci):
                wygranaKrupiera = True
                print("Krupier wygrywa! ")
                break
            elif punktyKrupiera(kartyKrupiera, wartosci) == punktyGracza(kartyGracza, wartosci):
                print("Remis! ")
                break


