from Domain.obiect import toString
from Logic.CRUD import adauga_obiect, sterge_obiect, modificareObiect
from Logic.Functionalitati import mutare_locatie, concatenare_string, determinare_pret


def printMenu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
    print("4. Schimbarea locatiei obiectelor")
    print("5. Concatenare unui string la descriere")
    print("6. Determinarea celui mai mare preț pentru fiecare locație")
    print("a. Afisare obiecte")
    print("x. Iesire")


def uiAdaugaObiect(lista):
    ID = input('Dati ID-ul: ')
    nume = input('Dati numele: ')
    descriere = input('Dati descrierea: ')
    pret_achizitie = input('Dati pretul de achizitie: ')
    locatie = input('Dati locatia: ')

    return adauga_obiect(ID, nume, descriere, pret_achizitie, locatie, lista)


def uiStergeObiect(lista):
    ID = input('Dati ID-ul pentru a sterge obiectul: ')
    return sterge_obiect(ID, lista)


def uiModificaObiect(lista):
    ID = input('Dati ID-ul pentru a modifica obiectul: ')
    nume = input('Dati numele pentru a modifica obiectul: ')
    descriere = input('Dati descrierea pentru a modifica obiectul: ')
    pret_achizitie = input('Dati pretul de achizitie pentru a modifica obiectul: ')
    locatie = input('Dati locatia pentru a modifica obiectul: ')
    return modificareObiect(ID, nume, descriere, pret_achizitie, locatie, lista)


def showAll(lista):
    for obiect in lista:
        print(toString(obiect))


def uiSchimbaLocatie(lista):
    locatie = input('Dati locatia noua: ')
    return mutare_locatie(locatie, lista)


def uiConcatenare(lista):
    valoare = input('Dati valoarea: ')
    stringul = input('Dati string-ul: ')
    return concatenare_string(valoare, stringul, lista)


def uiPretMaxim(lista):
    stringul = ''
    dictionar = determinare_pret(lista)
    for key,value in dictionar.items():
        stringul += f"Pretul cel mai mare pentru locatia '{key}' este de {value} lei.\n"
    return stringul


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == '1':
            lista = uiAdaugaObiect(lista)
        elif optiune == '2':
            lista = uiStergeObiect(lista)
        elif optiune == '3':
            lista = uiModificaObiect(lista)
        elif optiune == '4':
            lista = uiSchimbaLocatie(lista)
        elif optiune == '5':
            lista = uiConcatenare(lista)
        elif optiune == '6':
            print(uiPretMaxim(lista))
        elif optiune == 'a':
            showAll(lista)
        elif optiune == 'x':
            break
        else:
            print("Optiune gresita. Reincercati: ")
