#ID_438
from functions import liczba_pierwsza

ilosc_przypadkow = int(input("Ilość przypadków: "))
print("------------------------------------------------")

for i in range(ilosc_przypadkow):
    liczba = int(input("Podaj liczbę: "))

    liczba_pierwsza(liczba)