import os
os.system("clear")

# de mooie 3.9 code werkte niet goed dus ben ik door gegaan met de oude lelijke code.
productenlijst = {"appel": 199, "bannaan": 100, "vodka": 6000, "capri-sun": 1000000000, "gefermeteerdehockeyschoen": 100000000000000000000}


def productenlist():
    for key, value in productenlijst.items():
        print(key, value)


def overzicht():
    productenlist()


def toevoegen():
    product = input("welk product wil je tovoegen: ")
    prijs = input("hoe duur is het product: ")
    productenlijst[product] = int(prijs)
    productenlist()


def aanpassen():
    productenlist()
    producta = input("welk product wil je aanpassen: ")
    prijsa = input("Hoe duur word het product: ")
    productenlijst[producta] = prijsa
    productenlist()


def verwijderen():
    productenlist()
    productv = input("welk product wil je verwijderen: ")
    del productenlijst[productv]
    productenlist()

def boodschappen():
    prijstot = 0
    jaofne = input("wil je kopen of stoppen ja = kopen nee = stoppen: ")
    jaofnee = jaofne.lower()
    while jaofnee != "nee":
        jaofne = input("wil je kopen of stoppen ja = kopen nee = stoppen: ")
        jaofnee = jaofne.lower()
    #while (jaofnee := keuze()) != "nee":
        if jaofnee == "ja":
            productenlist()
            productb = str(input("welk product wil je kopen: "))
            prijstot += int(productenlijst[productb])
            print(prijstot)
        elif jaofnee == "nee":
            boodschappenprijs = boodschappen()
            boodschappenprijs = str(boodschappenprijs)
            print("De prijs van uw boodschappen is: €" + boodschappenprijs)
            return prijstot
        else:
            print("Fout, probeer iets anders.")

    boodschappenprijs = boodschappen()
    boodschappenprijs = str(boodschappenprijs)
    print("De prijs van uw boodschappen is: €" + boodschappenprijs)


#def maak_keuze():
    input_ = input("wat wil je doen overzicht = overzicht toevoegen = product toevoegen aanpassen = aanpassen verwijderen = verwijderen boodschappen = boodschappen doen stop = stoppen: ")
    letter = input_.lower()
    return letter


def main():
    input_ = input("wat wil je doen overzicht = overzicht toevoegen = product toevoegen aanpassen = aanpassen verwijderen = verwijderen boodschappen = boodschappen doen stop = stoppen: ")
    letter = input_.lower()
    while letter != "stop":
        input_ = input("wat wil je doen overzicht = overzicht toevoegen = product toevoegen aanpassen = aanpassen verwijderen = verwijderen boodschappen = boodschappen doen stop = stoppen: ")
        letter = input_.lower()   
    #while (letter := maak_keuze()) != "stop":
        if letter == "overzicht":
            overzicht()
        elif letter == "toevoegen":
            toevoegen()
        elif letter == "aanpassen":
            aanpassen()
        elif letter == "verwijderen":
            verwijderen()
        elif letter == "boodschappen":
            boodschappen()
        else:
            print("Fout, probeer iets anders.")
        # input_ = input("wat wil je doen o = overzicht t = product toevoegen a = aanpassen v = verwijderen b = boodschappen doen stop = stoppen: ")
        # letter = input_.lower()
main()