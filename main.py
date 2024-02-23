#ID_496

from functions import dwie_cyfry_silni

ilosc_przypadkow = int(input("Ilość przypadkow: "))
print("------------------------------------------------")

for i in range(ilosc_przypadkow):
    liczba = int(input("Podaj liczbę: "))

    dwie_cyfry_silni(liczba)