from Domain.obiect import toString
from Logic.CRUD import adauga_obiect, modificareObiect, sterge_obiect


def show_all(lista):
    for obiect in lista:
        print(toString(obiect))


def meniu_help():
    print("Add, ID, nume, descriere, pret achizitie, locatie -> Adauga obiectul")
    print("Update, ID, nume, descriere, pret achizitie, locatie -> Modifica obiectul")
    print("Delete, ID -> Sterge obiectul")
    print("ShowAll -> Afiseaza obiectele din lista")
    print("Stop -> Oprire program")


def menu(lista):
    while True:
        optiune = input()
        if optiune == 'Help':
            meniu_help()
        else:
            optiuni = optiune.split(';')
            if optiuni[0] == 'Stop':
                break
            else:
                for optiune in optiuni:
                    comenzi = optiune.split(',')
                    if comenzi[0] == 'Add':
                        try:
                            lista = adauga_obiect(comenzi[1], comenzi[2], comenzi[3], comenzi[4], comenzi[5], lista)
                        except ValueError as ve:
                            print('Eroare: ', ve)
                    elif comenzi[0] == 'ShowAll':
                        show_all(lista)
                    elif comenzi[0] == 'Update':
                        lista = modificareObiect(comenzi[1], comenzi[2], comenzi[3], comenzi[4], comenzi[5], lista)
                    elif comenzi[0] == 'Delete':
                        lista = sterge_obiect(comenzi[1], lista)
                    else:
                        print("Optiunea este gresita, tastati 'Help' pentru a vedea optiunile disponibile.")