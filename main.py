# ID_769
from functions import zadanie_probne

print("Liczba A i B mniejsze od 200.")
A = int(input("Podaj A: "))
B = int(input("Podaj B: "))
if A < 200 and B < 200:
    zadanie_probne(A, B)
else:
    print("Liczba spoza zakresu :(")


