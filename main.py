# ID_663

from functions import sort_1

ilosc_testow = int(input("Ilość testów: "))
print("-------------------------------------------------")

for i in range(ilosc_testow):
    liczba_punktow = int(input("Liczba punktów: "))

    lista_nazwy = []
    lista_wspolrzedne_x = []
    lista_wspolrzedne_y = []

    for j in range(liczba_punktow):
        nazwa = input("Podaj wielką literę jako nazwę punktu: ")
        wspolrzedna_x = int(input("Podaj współrzędną x: "))
        wspolrzedna_y = int(input("Podaj współrzędną y: "))
        lista_nazwy.append(nazwa)
        lista_wspolrzedne_x.append(wspolrzedna_x)
        lista_wspolrzedne_y.append(wspolrzedna_y)

    sort_1(lista_nazwy,lista_wspolrzedne_x,lista_wspolrzedne_y)



