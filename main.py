# ID_723
from functions import ROL

ilosc_testow = int(input("Ilość testów: "))
print("-------------------------------------------------------")

for i in range(ilosc_testow):
    test = []
    ilosc_liczb = int(input("Ilość liczb: "))
    print("Podaj liczby:")
    for j in range(ilosc_liczb):
        liczba = input()
        test.append(liczba)
    ROL(test)
    print("-------------------------------------------------------")



