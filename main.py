#ID_506

from functions import flamaster

ilosc_przypadkow = int(input("Ilość przypadkow: "))
print("------------------------------------------------")

for i in range(ilosc_przypadkow):
    litery = input("Podaj duże litery: ")
    flamaster(litery)
