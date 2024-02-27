# ID_617


def string_merge(str_1, str_2):
    wynik = ""

    if len(str_1) <= len(str_2):
        ilosc_iteracji = len(str_1)
    else:
        ilosc_iteracji = len(str_2)

    for i in range(ilosc_iteracji):
        str_3 = str_1[i] + str_2[i]
        wynik = wynik + str_3
    print("Wynik:",wynik)
    print("-----------------------------------------------------")
