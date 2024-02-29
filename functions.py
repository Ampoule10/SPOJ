# ID_675

def skarb_finder(lista_kierunek, lista_kroki):
    suma_x = 0
    suma_y = 0

    for i in range(len(lista_kierunek)):
        if lista_kierunek[i] == 0:
            suma_y = suma_y + lista_kroki[i]
        elif lista_kierunek[i] == 1:
            suma_y = suma_y - lista_kroki[i]
        elif lista_kierunek[i] == 2:
            suma_x = suma_x - lista_kroki[i]
        elif lista_kierunek[i] == 3:
            suma_x = suma_x + lista_kroki[i]

    if suma_x == 0 and suma_y == 0:
        print("-------------------------------------------")
        print("STUDNIA")
    elif suma_x == 0:
        print("-------------------------------------------")
        print(suma_x, suma_y)
    elif suma_y == 0:
        print("-------------------------------------------")
        print(suma_x, suma_y)
    else:
        if suma_y > 0:
            if suma_x > 0:
                print("-------------------------------------------")
                print(0, suma_y)
                print(3, suma_x)
            elif suma_x < 0:
                print("-------------------------------------------")
                print(0, suma_y)
                print(2, -suma_x)
        elif suma_y < 0:
            if suma_x > 0:
                print("-------------------------------------------")
                print(1, -suma_y)
                print(3, suma_x)
            elif suma_x < 0:
                print("-------------------------------------------")
                print(1, -suma_y)
                print(2, -suma_x)
    print("-------------------------------------------")

    # print("Lista kierunek:", lista_kierunek)
    # print("Lista kroki:", lista_kroki)
    # print("-------------------------------------------")
