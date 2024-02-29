# ID_675
from functions import skarb_finder

ilosc_testow = int(input("Podaj ilość testów: "))
print("-------------------------------------------")

for i in range(ilosc_testow):
    ilosc_zestawow = int(input("Podaj ilość zestawów: "))

    lista_kierunek = []
    lista_kroki = []

    for j in range(ilosc_zestawow):
        kierunek = int(input("Podaj cyfrę (kierunek): "))
        kroki = int(input("Podaj cyfrę (ilość kroków): "))
        lista_kierunek[len(lista_kierunek):] = [kierunek]
        lista_kroki[len(lista_kroki):] = [kroki]
    skarb_finder(lista_kierunek, lista_kroki)
