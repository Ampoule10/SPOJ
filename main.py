# ID_804
from functions import gra_euklidesa

liczba_partii = int(input("Liczba partii: "))
print("-------------------------------------------")

nadlista = []

for i in range(liczba_partii):
    para_ab = []
    zetony_a = int(input("Podaj a: "))
    para_ab.append(zetony_a)
    zetony_b = int(input("Podaj b: "))
    para_ab.append(zetony_b)
    nadlista.append(para_ab)

print("-------------------------------------------")
gra_euklidesa(nadlista)

# a = [1,1]
# b = [2,4]
# c = [9,6]
# nadlista = []
# nadlista.append(a)
# nadlista.append(b)
# nadlista.append(c)
# print(nadlista)


