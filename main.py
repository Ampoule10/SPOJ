# ID_606

from functions import odwrocona_tablica

ilosc_przypadkow = int(input("Ilość przypadków: "))

for i in range(ilosc_przypadkow):
    print("---------------------------------------------------------------------")
    ile_liczb = int(input("Ile liczb? : "))
    odwrocona_tablica(ile_liczb)


#######################################################################################

# from functions import odwrocona_tablica
#
# ilosc_przypadkow = int(input("Ilość przypadkow: "))
# print("------------------------------------------------")
#
# for i in range(ilosc_przypadkow):
#     ilosc_liczb = int(input("Ile liczb?: "))
#     liczby = input("Podaj liczby oddzielone JEDNĄ spacją: ").split()
#     odwrocona_tablica(liczby,ilosc_liczb)
