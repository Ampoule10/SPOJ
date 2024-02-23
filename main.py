# ID_601

from functions import NWD


ilosc_przypadkow = int(input("Ilość przypadkow: "))
print("------------------------------------------------")

for i in range(ilosc_przypadkow):
    liczba_1 = int(input("Podaj liczbę 1: "))
    liczba_2 = int(input("Podaj liczbę 2: "))
    NWD(liczba_1,liczba_2)
