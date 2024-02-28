# ID_626

from functions import obzartuchy

ilosc_testow = int(input("Ilość testów: "))
print("-------------------------------------------------")

for i in range(ilosc_testow):
    ilosc_obzartuchow = int(input("Ilość obżartuchów: "))
    ilosc_ciastek_w_pudelku = int(input("Ilość ciastek w pudełku: "))

    wszystkie_czasy = []

    for j in range(ilosc_obzartuchow):
        print("Czas jedzenia jednego ciastka przez obżartucha numer", (j+1))
        jeden_czas = int(input("(Podaj czas w sekundach): "))
        wszystkie_czasy.append(jeden_czas)
    obzartuchy(ilosc_ciastek_w_pudelku, wszystkie_czasy)



