# ID_606

def odwrocona_tablica(ile_liczb):
    liczby = []
    for j in range(ile_liczb):
        liczba = input("Podaj liczbę: ")
        liczby.append(liczba)
    odwrocone = liczby[::-1]
    print("Początkowa kolejność:", liczby)
    print("Odwrócona kolejność:", odwrocone)


########################################################################################
# def odwrocona_tablica(liczby,ilosc_liczb):
#
#     odwrocona = liczby[::-1]
#     if len(liczby) != ilosc_liczb:
#         print("Niepoprawna ilość liczb :(")
#         print("------------------------------------------------")
#     else:
#         print("Odwrócona kolejność liczb:",odwrocona)
#         print("------------------------------------------------")