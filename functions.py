# ID_708

def Collatz(lista):
    print("Ilość kroków potrzebnych do osiągnięcia wartości 1 dla każdej z podanych liczb w sekwencji Collatza:")
    for i in (lista):
        x = i
        counter = 0
        while i != 1:
            if i % 2 != 0:
                i = 3 * i + 1
                counter = counter + 1
            elif i % 2 == 0:
                i = i / 2
                counter = counter + 1
        print("Liczba:", x, "| Ilość kroków:", counter)
