from Domain.obiect import toString
from Logic.CRUD import adauga_obiect, sterge_obiect, modificareObiect
from Logic.Functionalitati import mutare_locatie, concatenare_string, determinare_pret, sortare_dupa_pret, \
    afisarea_sumelor_locatii


def printMenu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
    print("4. Schimbarea locatiei obiectelor")
    print("5. Concatenare unui string la descriere")
    print("6. Determinarea celui mai mare preț pentru fiecare locație")
    print("7. Ordonare dupa pret")
    print("8. Afișarea sumelor prețurilor pentru fiecare locație")
    print("9. Undo")
    print("10. Redo")
    print("a. Afisare obiecte")
    print("x. Iesire")


def uiAdaugaObiect(lista):
    try:
        ID = input('Dati ID-ul: ')
        nume = input('Dati numele: ')
        descriere = input('Dati descrierea: ')
        pret_achizitie = input('Dati pretul de achizitie: ')
        locatie = input('Dati locatia: ')
        return adauga_obiect(ID, nume, descriere, pret_achizitie, locatie, lista)
    except ValueError as ve:
        print("Eroare:", ve)
        return lista



def uiStergeObiect(lista):
    try:
        ID = input('Dati ID-ul pentru a sterge obiectul: ')
        return sterge_obiect(ID, lista)
    except ValueError as ve:
        print("Eroare:", ve)
        return lista


def uiModificaObiect(lista):
    try:
        ID = input('Dati ID-ul pentru a modifica obiectul: ')
        nume = input('Dati numele pentru a modifica obiectul: ')
        descriere = input('Dati descrierea pentru a modifica obiectul: ')
        pret_achizitie = input('Dati pretul de achizitie pentru a modifica obiectul: ')
        locatie = input('Dati locatia pentru a modifica obiectul: ')
        return modificareObiect(ID, nume, descriere, pret_achizitie, locatie, lista)
    except ValueError as ve:
        print("Eroare:", ve)
        return lista


def showAll(lista):
    for obiect in lista:
        print(toString(obiect))


def uiSchimbaLocatie(lista):
    try:
        locatie = input('Dati locatia noua: ')
        return mutare_locatie(locatie, lista)
    except ValueError as ve:
        print("Eroare:", ve)
        return lista


def uiConcatenare(lista):
    try:
        valoare = input('Dati valoarea: ')
        stringul = input('Dati string-ul: ')
        return concatenare_string(valoare, stringul, lista)
    except ValueError as ve:
        print("Eroare:", ve)
        return lista


def uiPretMaxim(lista):
    stringul = ''
    dictionar = determinare_pret(lista)
    for key, value in dictionar.items():
        stringul += f"Pretul cel mai mare pentru locatia '{key}' este de {value} lei.\n"
    return stringul


def uiOrdonare(lista):
    showAll(sortare_dupa_pret(lista))


def uiPretDupaLocatie(lista):
    print(afisarea_sumelor_locatii(lista))


def runMenu(lista):
    temp = 0

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
        elif optiune == '7':
            print(uiOrdonare(lista))
        elif optiune == '8':
            print(uiPretDupaLocatie(lista))
        elif optiune == '9': #Undo
            if temp == 0:
                element_sters = lista.pop()
                temp += 1
        elif optiune == '10': #Redo
            if temp > 0:
                lista.append(element_sters)
                temp -= 1
        elif optiune == 'a':
            showAll(lista)
        elif optiune == 'x':
            break
        else:
            print("Optiune gresita. Reincercati: ")
