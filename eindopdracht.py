import os
os.system("clear")

productenlijst = {"appel": 199, "bannaan": 100, "vodka": 6000, "capri-sun": 1000000000, "gefermeteerdehockeyschoen": 100000000000000000000}




def productenlist():
    for key, value in productenlijst.items():
        print(key, value)
while True:
    inputt = input("wat wil je doen o = overzicht t = product toevoegen a = aanpassen v = verwijderen b = boodschappen doen stop = stoppen: ")
    letter = inputt.lower()
    if letter == "o":
        productenlist()
    elif letter == "t":
        product = input("welk product wil je tovoegen: ")
        prijs = input("hoe duur is het product: ")
        productenlijst[product] = int(prijs)
        productenlist()
    elif letter == "a":
        productenlist()
        producta = input("welk product wil je aanpassen: ")
        prijsa = input("Hoe duur word het product: ")
        productenlijst[producta] = prijsa
        productenlist()
    elif letter == "v":
        productenlist()
        productv = input("welk product wil je verwijderen: ")
        del productenlijst[productv]
        productenlist()
    elif letter == "b":
        def boodschappendoen():
            prijstot = 0
            while True:
                jaofne = input("wil je kopen of stoppen ja = kopen nee = stoppen: ")
                jaofnee = jaofne.lower()
                if jaofnee == "ja":
                    productenlist()
                    productb = str(input("welk product wil je kopen: "))
                    prijstot += int(productenlijst[productb])
                    print(prijstot)
                elif jaofnee == "nee":
                    print()
                    return prijstot
                else:
                    print("Fout, probeer iets anders.")

        boodschappenprijs = boodschappendoen()
        boodschappenprijs = str(boodschappenprijs)
        print("De prijs van uw boodschappen is: €" + boodschappenprijs)

    elif letter == "stop":
        break
    else:
        print("Fout, probeer iets anders.")