#ID_499

from functions import potegowanie

ilosc_przypadkow = int(input("Ilość przypadkow: "))
print("------------------------------------------------")

for i in range(ilosc_przypadkow):
    podstawa = int(input("Podaj podstawę: "))
    wykladnik = int(input("Podaj wykładnik: "))
    potegowanie(podstawa, wykladnik)