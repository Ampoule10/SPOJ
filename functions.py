# ID_506
def flamaster(litery):
    licznik = 1
    for i in range(len(litery) - 1):
        if litery[i] != litery[i + 1]:
            if licznik == 1:
                print(litery[i], end=" ")
                licznik = 1
            elif licznik == 2:
                print(litery[i - 1], litery[i], end=" ")
                licznik = 1
            elif licznik > 2:
                print(litery[i], licznik, end=" ")
                licznik = 1
        else:
            licznik += 1

    if licznik == 1:
        print(litery[len(litery) - 1])
        licznik = 1
    elif licznik == 2:
        print(litery[len(litery) - 1], litery[len(litery) - 1])
        licznik = 1
    elif licznik > 2:
        print(litery[len(litery) - 1], licznik)
        licznik = 1

    print("------------------------------------------------")
