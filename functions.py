#ID_522

def przedszkolanka(l_1,l_2):

    nww = 0

    for i in range(l_1*l_2):
        wielokrotnosc_1 = l_1 * (i+1)
        for j in range(l_1*l_2):
            wielokrotnosc_2 = l_2 * (j+1)
            if wielokrotnosc_2 > wielokrotnosc_1:
                break
            elif wielokrotnosc_2 == wielokrotnosc_1:
                nww = wielokrotnosc_2
                print("Najmniejsza wspólna wielokrotność:", nww)
                print("------------------------------------------------")
        if nww > 0:
            break



