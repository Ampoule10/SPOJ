# ID_568

def  Zabawne_Dodawanie_Piotrusia(l_1):
    if l_1 == l_1[::-1]:
        print("Palindrom:",l_1,"Liczba dodawań:",0)
    else:
        licznik = 0
        while l_1 != l_1[::-1]:
            suma = int(l_1) + int(l_1[::-1])
            suma = str(suma)
            l_1 = suma
            licznik += 1
        print("Palindrom:",l_1,"Liczba dodawań:",licznik)
        print("------------------------------------------------")




