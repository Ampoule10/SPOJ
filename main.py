# ID_708
from functions import Collatz

ilosc_testow = int(input("Podaj ilość testów: "))
print("Podaj wartości testów:")

lista = []

for i in range(ilosc_testow):
    wartosc_testu = int(input())
    lista.append(wartosc_testu)

Collatz(lista)
