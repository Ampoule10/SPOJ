# ID_601

def NWD(l_1, l_2):

    dzielniki_1 = []
    dzielniki_2 = []

    for i in range(l_1):
        if l_1 % (i + 1) == 0:
            dzielniki_1.append(i + 1)

    for i in range(l_2):
        if l_2 % (i + 1) == 0:
            dzielniki_2.append(i + 1)

    wspolne_dzielniki = []

    for i in range(len(dzielniki_1)):
        x = dzielniki_1[i]
        for j in range(len(dzielniki_2)):
            y = dzielniki_2[j]
            if x == y:
                nwd = x

    print("NWD =", nwd)
    print("------------------------------------")




