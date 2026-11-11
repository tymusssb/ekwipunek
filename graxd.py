import random

def oblicz_ciezar(eq):
    ciezar = 0
    for przedmiot in eq:
        ciezar += eq[przedmiot]["ilosc"]*eq[przedmiot]["waga"]
    return(ciezar)

def sprawdz_przedmiot(eq):
    sprawdzanie = input("Jaki przedmiot sprawdzamy byczku?: ")
    if sprawdzanie in eq:
        return("Przedmiot " + sprawdzanie + " jest w EQ!")
    else:
        return("Przedmiotu " + sprawdzanie + " nie ma w EQ...")

def pokaz_przedmioty(eq):
    for przedmiot in eq:
        print(przedmiot, eq[przedmiot]["ilosc"])

def uzyj_przedmiot(eq, ciezar):
    uzycie = input("Który przedmiot chcesz użyć?: ")
    if uzycie not in eq:
        return("Przedmiotu " + uzycie + " nie można użyć (nie ma go w EQ)")
    ciezar -= eq[uzycie]["waga"]
    eq[uzycie]["ilosc"] -= 1
    if eq[uzycie]["ilosc"] < 1:
        del eq[uzycie]
    return("Przedmiot został zużyty")

def dodaj_przedmiot(eq):
    przedmiot = input("Jaki przedmiot chcesz dodać byku?: ")
    if przedmiot in eq:
        eq[przedmiot]["ilosc"] += 1
    if przedmiot not in eq:
        eq[przedmiot] = {"ilosc": 1,
                         "waga": random.randint(5, 10),
                         "wartosc": random.randint(10, 20)}
    return()

def gra():
    ekwipunek = {"miecz": {"ilosc": 1, 
                           "waga": 2.5, 
                           "wartosc": 40}, 
                 "mikstura": {"ilosc": 3, 
                              "waga": 0.1, 
                              "wartosc": 15}, 
                 "zloto": {"ilosc": 50, 
                           "waga": 0.1, 
                           "wartosc": 1}}
    limit = 60
    ciezar = oblicz_ciezar(ekwipunek)
    print("===MENU===")
    print("1. Pokaż przedmioty")
    print("2. Dodaj przedmiot")
    print("3. Użyj przedmiotu")
    print("4. Sprawdź przedmiot")
    print("5. Wyjdź")
    while True:
        wybor = int(input("Co chcesz zrobić?: "))
        if wybor == 1:
            pokaz_przedmioty(ekwipunek)
        elif wybor == 2:
            dodaj_przedmiot(ekwipunek)
        elif wybor == 3:
            print(uzyj_przedmiot(ekwipunek, ciezar))
        elif wybor == 4:
            print(sprawdz_przedmiot(ekwipunek))
        elif wybor == 5:
            break
gra()