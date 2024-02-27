# ID_609
import math


def pole_pewnego_kola(r, d):
    if d >= 2 * r:
        wynik = 0.00
    elif d == 0:
        wynik = math.pi * r * r
    else:
        r_szukanego_kola = math.sqrt((r * r) - ((d / 2) * (d / 2)))
        wynik = math.pi * r_szukanego_kola * r_szukanego_kola
        zaokraglony_wynik = round(wynik, 2)
        print("Wynik:", zaokraglony_wynik)
