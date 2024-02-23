def liczba_pierwsza(l_1):
    counter = 0
    for i in range(l_1):
        if l_1 % (i+1) == 0:
            counter += 1
    if counter == 2:
        print("TAK, to jest liczba pierwsza.")
        print("------------------------------------------------")
    else:
        print("NIE, to nie jest liczba pierwsza.")
        print("------------------------------------------------")
