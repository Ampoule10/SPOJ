# ID_626

def obzartuchy(ilosc_ciastek_w_pudelku, wszystkie_czasy):

    suma_ciastek = 0

    for i in range(len(wszystkie_czasy)):
        ilosc_ciastek = 86400 // wszystkie_czasy[i]
        suma_ciastek += ilosc_ciastek

    if suma_ciastek % ilosc_ciastek_w_pudelku == 0:
        ilosc_pudelek = suma_ciastek // ilosc_ciastek_w_pudelku
    else:
        ilosc_pudelek = suma_ciastek // ilosc_ciastek_w_pudelku + 1

    print("Ilość potrzebnych pudełek:", ilosc_pudelek)
    print("-------------------------------------------------")