from Domain.obiect import toString
from Logic.CRUD import adauga_obiect, modificareObiect, sterge_obiect


def show_all(lista):
    if lista:
        for obiect in lista:
            print(toString(obiect))
    else:
        print('Nu exista obiecte in lista!')


def meniu_help():
    print("Add;ID, nume, descriere, pret achizitie, locatie -> Adauga obiectul")
    print("Update;ID, nume, descriere, pret achizitie, locatie -> Modifica obiectul")
    print("Delete;ID -> Sterge obiectul")
    print("ShowAll -> Afiseaza obiectele din lista")
    print("Stop -> Oprire program")


def menu(lista):
    print("Nota: daca ai nevoie de ajutor, scrie 'Help'.")
    while True:
        optiune = input()
        if optiune == 'Help':
            meniu_help()
        else:
            optiuni = optiune.split(';')
            if optiuni[0] == 'Stop':
                break
            else:
                    if optiuni[0] == 'Add':
                        comenzi = optiune[4:].split(', ')
                        try:
                            lista = adauga_obiect(comenzi[0], comenzi[1], comenzi[2], float(comenzi[3]), comenzi[4], lista)
                            print('Obiectul a fost adaugat.')
                        except ValueError as ve:
                            print('Eroare: ', ve)
                    elif optiuni[0] == 'ShowAll':
                        show_all(lista)
                    elif optiuni[0] == 'Update':
                        comenzi = optiune[7:].split(', ')
                        try:
                            lista = modificareObiect(comenzi[0], comenzi[1], comenzi[2], float(comenzi[3]), comenzi[4], lista)
                            print('Obiectul a fost modificat.')
                        except ValueError as ve:
                            print('Eroare: ', ve)
                    elif optiuni[0] == 'Delete':
                        comenzi = optiune[7:].split(', ')
                        try:
                            lista = sterge_obiect(comenzi[0], lista)
                            print('Obiectul a fost sters.')
                        except ValueError as ve:
                            print('Eroare: ', ve)
                    else:
                        print("Optiunea este gresita, tastati 'Help' pentru a vedea optiunile disponibile.")


menu([])
