# ID_663

def sort_1(lista_1, lista_2, lista_3):
    lista_odleglosci = []
    lista_stringow = []

    for i in range(len(lista_1)):
        odleglosc = pow(pow(lista_2[i], 2) + pow(lista_3[i], 2), 0.5)
        zaokraglona_odleglosc = round(odleglosc, 2)
        lista_odleglosci.append(zaokraglona_odleglosc)
        nazwa_i_wspolrzedne = lista_1[i] + " " + str(lista_2[i]) + " " + str(lista_3[i])
        lista_stringow.append(nazwa_i_wspolrzedne)

    dictionary = {}

    posortowane = sorted(lista_odleglosci)
    print("Posortowanie względem odległości od środka układu współrzędnych:")
    for key in posortowane:
        value = lista_stringow[lista_odleglosci.index(key)]
        # value = lista_stringow[posortowane.index(key)]
        print(value)
    print("-------------------------------------------------")
    print("Lista stringów:", lista_stringow)
    print("Lista odległości:", lista_odleglosci)
    # print("Lista odległości po sortowaniu:", posortowane)
    print("Lista odległości po sortowaniu:", posortowane)
    print("-------------------------------------------------")
