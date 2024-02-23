#ID_522

from functions import przedszkolanka

ilosc_przypadkow = int(input("Ilość przypadkow: "))
print("------------------------------------------------")

for i in range(ilosc_przypadkow):
    grupa_1 = int(input("Podaj ilość w grupie 1: "))
    grupa_2 = int(input("Podaj ilość w grupie 2: "))
    przedszkolanka(grupa_1,grupa_2)
