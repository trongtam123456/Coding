lemon = [5, 5, 10, 20]
to5 = []
to10 = []
to20 = []
for i in range(0, len(lemon)):
    #doi voi khach dua to 5
    if (lemon[i] == 5):
        to5.append(5)
    #doi voi khach dua to 10
    elif (lemon[i] == 10):
        #them 1 to 10, bot 1 to 5
        if (len(to5) < 1):
            print(False)
            break
        else:
            to5.remove(5)
            to10.append(10)
    elif (lemon[i] == 20):
        if (len(to10) >= 1 and len(to5) >= 1):
            to10.remove(10)
            to5.remove(5)
            to20.append(20)
        elif (len(to5) > 3):
            to5.remove(5)
            to5.remove(5)
            to5.remove(5)
            to20.append(20)
        else:
            print(False)
            break
    else:
        print(True)



