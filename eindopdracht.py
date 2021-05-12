import os
os.system("clear")


def productenlist(productenlijst):
    for key, value in productenlijst.items():
        print(key, value)


def overzicht(productenlijst):
    productenlist(productenlijst)


def toevoegen(productenlijst):
    product = input("welk product wil je tovoegen: ")
    prijs = input("hoe duur is het product: ")
    productenlijst[product] = int(prijs)
    productenlist(productenlijst)
    return productenlijst


def aanpassen(productenlijst):
    productenlist(productenlijst)
    producta = input("welk product wil je aanpassen: ")
    prijsa = input("Hoe duur word het product: ")
    productenlijst[producta] = prijsa
    productenlist(productenlijst)
    return productenlijst


def verwijderen(productenlijst):
    productenlist(productenlijst)
    productv = input("welk product wil je verwijderen: ")
    del productenlijst[productv]
    productenlist(productenlijst)
    return productenlijst

def boodschappen(productenlijst):
    prijstot = 0
    jaofne = input("wil je kopen of stoppen ja = kopen nee = stoppen: ")
    jaofnee = jaofne.lower()
    while jaofnee != "nee":
        if jaofnee == "ja":
            productenlist(productenlijst)
            productb = str(input("welk product wil je kopen: "))
            prijstot += int(productenlijst[productb])
            print(prijstot)
        elif jaofnee == "nee":
            boodschappenprijs = str(boodschappenprijs)
            print("De prijs van uw boodschappen is: €" + boodschappenprijs)
            return prijstot
        else:
            print("Fout, probeer iets anders.")
        jaofne = input("wil je kopen of stoppen ja = kopen nee = stoppen: ")
        jaofnee = jaofne.lower()


def main():
    productenlijst = {"appel": 199, "bannaan": 100, "vodka": 6000, "capri-sun": 1000000000, "gefermeteerdehockeyschoen": 100000000000000000000}
    input_ = input("wat wil je doen overzicht = overzicht toevoegen = product toevoegen aanpassen = aanpassen verwijderen = verwijderen boodschappen = boodschappen doen stop = stoppen: ")
    letter = input_.lower()
    while letter != "stop":
        if letter == "overzicht":
            overzicht(productenlijst)
        elif letter == "toevoegen":
            productenlijst = toevoegen(productenlijst)
        elif letter == "aanpassen":
            productenlijst = aanpassen(productenlijst)
        elif letter == "verwijderen":
            productenlijst = verwijderen(productenlijst)
        elif letter == "boodschappen":
            boodschappen(productenlijst)
        else:
            print("Fout, probeer iets anders.")
        input_ = input("wat wil je doen overzicht = overzicht toevoegen = product toevoegen aanpassen = aanpassen verwijderen = verwijderen boodschappen = boodschappen doen stop = stoppen: ")
        letter = input_.lower()
main()