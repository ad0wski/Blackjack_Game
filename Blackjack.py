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

Powodzenia! 🍀"""

print(zasady)

def gra():
    wartosci = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "J": 10, "Q": 10, "K": 10, "A": 11  # lub 1 w zależności od sytuacji
    }

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


    #ZLICZENIE PUNKTOW KART
    def policz_punkty(karty, wartosci):
        punkty = 0
        asy = 0
        for karta in karty:
            wartoscKarty = karta[:-2]
            punkty += wartosci[wartoscKarty]
            if wartoscKarty == "A":
                asy += 1
        # zamiana Asa z 11 na 1, jeśli trzeba
        while punkty > 21 and asy > 0:
            punkty -= 10
            asy -= 1
        return punkty

    rozdanieKartDlaGracza(kartyGracza, dostepneKartyWTalii)
    rozdanieKartDlaKrupiera(kartyKrupiera, dostepneKartyWTalii)

    print("\n-------------------- NOWA GRA --------------------\n")

    print("Karty gracza:", kartyGracza, "=> punkty:", policz_punkty(kartyGracza, wartosci))
    print("Karty krupiera:", [kartyKrupiera[0], "??"], "punkty:", policz_punkty([kartyKrupiera[0]], wartosci)) # tylko 1 karta widoczna


    #DOBIERANIE KART PRZEZ GRACZA
    punktyKartGracza = policz_punkty(kartyGracza, wartosci)
    czyGraczPrzegral = False
    while True:
        decyzja = input("Dobierasz kartę (h) czy pasujesz (s)? ")
        if decyzja == "h":
            wylosowanaKarta = dostepneKartyWTalii[random.randint(0, len(dostepneKartyWTalii) - 1)]
            kartyGracza.append(wylosowanaKarta)
            dostepneKartyWTalii.remove(wylosowanaKarta)
            punktyKartGracza = policz_punkty(kartyGracza, wartosci)
            print("Karty gracza:", kartyGracza, "=> punkty:", punktyKartGracza)
            if punktyKartGracza == 21:
                break
            elif punktyKartGracza > 21:
                print("\nKrupier wygrywa! (gracz bust)")
                czyGraczPrzegral = True
                break
            else:
                continue
        elif decyzja == "s":
            print("\n-------------------- TURA KRUPIERA --------------------\n")
            print("Karty krupiera:", kartyKrupiera, "=> punkty:", policz_punkty(kartyKrupiera, wartosci))
            break
        else:
            print("Blad! Wpisz 'h' albo 's'. ")


    # DOBIERANIE KART PRZEZ KRUPIERA
    if czyGraczPrzegral == False:
        while True:
            if policz_punkty(kartyKrupiera, wartosci) < 17:
                wylosowanaKarta = dostepneKartyWTalii[random.randint(0, len(dostepneKartyWTalii) - 1)]
                kartyKrupiera.append(wylosowanaKarta)
                dostepneKartyWTalii.remove(wylosowanaKarta)
                print("Karty krupiera:", kartyKrupiera, "=> punkty:", policz_punkty(kartyKrupiera, wartosci))
                if policz_punkty(kartyKrupiera, wartosci) > 21:
                    print("\nGracz wygrywa! (krupier bust) ")
                    break
                elif policz_punkty(kartyKrupiera, wartosci) == 21 and punktyKartGracza == 21:
                    print("\nRemis! ")
                    break
                elif policz_punkty(kartyKrupiera, wartosci) >= 17 and policz_punkty(kartyKrupiera, wartosci) < 21:
                    if policz_punkty(kartyKrupiera, wartosci) < punktyKartGracza:
                        print("\nGracz wygrywa! ")
                        break
                    elif policz_punkty(kartyKrupiera, wartosci) > punktyKartGracza:
                        print("\nKrupier wygrywa! ")
                        break
                    elif policz_punkty(kartyKrupiera, wartosci) == punktyKartGracza:
                        print("\nRemis! ")
                        break
                else:
                    continue
            else:
                if policz_punkty(kartyKrupiera, wartosci) < punktyKartGracza:
                    print("\nGracz wygrywa! ")
                    break
                elif policz_punkty(kartyKrupiera, wartosci) > punktyKartGracza:
                    print("\nKrupier wygrywa! ")
                    break
                elif policz_punkty(kartyKrupiera, wartosci) == punktyKartGracza:
                    print("\nRemis! ")
                    break

    print("\n-------------------- KONIEC GRY --------------------\n")
    pass


while True:
    gra()
    koniecGry = input("Czy chcesz zakonczyc gre? (y / n): ".lower())
    if koniecGry == "y":
        print("Dzięki za grę! Do zobaczenia :)")
        break