#ID_496
def dwie_cyfry_silni(l_1):
    silnia = 1
    for i in range(l_1):
        silnia = silnia * (i+1)

    print("Silnia:",silnia)
    print("Liczba dziesiątek:", silnia // 10 % 10)
    print("liczba jedności:", silnia % 10)
    print("------------------------------------------------")
