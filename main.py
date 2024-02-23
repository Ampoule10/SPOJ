# ID_549

from functions import proste_dodawanie

ilosc_przypadkow = int(input("Ilość przypadkow: "))
print("------------------------------------------------")

for i in range(ilosc_przypadkow):
    ilosc_liczb = int(input("Podaj ilość liczb: "))
    liczby = []
    for i in range(ilosc_liczb):
        liczba = int(input("Podaj liczbę: "))
        liczby.append(liczba)
    proste_dodawanie(liczby)
