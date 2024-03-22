# ID_804

def gra_euklidesa(nadlista):
    for podlista in nadlista:
        tmp_1 = podlista[0]
        tmp_2 = podlista[1]
        while podlista[0] != podlista[1]:
            if podlista[0] > podlista[1]:
                podlista[0] = podlista[0] - podlista[1]
            elif podlista[1] > podlista[0]:
                podlista[1] = podlista[1] - podlista[0]
        wyjscie = podlista[0] + podlista[1]
        print("Dla partii", tmp_1, tmp_2, ":", wyjscie)
