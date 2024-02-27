# ID_617
from functions import string_merge

ilosc_testow = int(input("Podaj ilosc testow: "))
print("-----------------------------------------------------")

for i in range(ilosc_testow):
    str_1 = input("Pierwszy string: ")
    str_2 = input("Drugi string: ")
    string_merge(str_1, str_2)
