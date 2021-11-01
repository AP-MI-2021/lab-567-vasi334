from Domain.obiect import creeaza_obiect, getID, getNume, getDescriere, getPretAchizitie, getLocatie


def mutare_locatie(locatie, lista):
    lista_noua = []
    for obiect in lista:
        lista_noua.append(creeaza_obiect(getID(obiect), getNume(obiect),
                                         getDescriere(obiect), getPretAchizitie(obiect), locatie))

    return lista_noua


def concatenare_string(valoare, stringul, lista):
    lista_noua = []
    for obiect in lista:
        if getPretAchizitie(obiect) > float(valoare):
            lista_noua.append(creeaza_obiect(getID(obiect), getNume(obiect),getDescriere(obiect) + stringul,
                                             getPretAchizitie(obiect), getLocatie(obiect)))
        else:
            lista_noua.append(obiect)

    return lista_noua


def gasire_locatii(lista):
    lista_locatii = []
    for obiect in lista:
        if getLocatie(obiect) not in lista_locatii:
            lista_locatii.append(getLocatie(obiect))

    return lista_locatii


def determinare_pret(lista):
    locatii = gasire_locatii(lista)
    dictionar_preturi_locatii = {}
    for locatie in locatii:
        maximum = None
        for obiect in lista:
            if maximum is None and getLocatie(obiect) == locatie:
                maximum = getPretAchizitie(obiect)
            elif getLocatie(obiect) == locatie and getPretAchizitie(obiect) > maximum:
                maximum = getPretAchizitie(obiect)

        dictionar_preturi_locatii[f'{locatie}'] = maximum

    return dictionar_preturi_locatii


def sortare_dupa_pret(lista):
    lista_sortata = sorted(lista, key=lambda obiect: getPretAchizitie(obiect))
    return lista_sortata


def afisarea_sumelor_locatii(lista):
    dict_preturi = {}
    lista_locatii = gasire_locatii(lista)

    for locatie in lista_locatii:
        suma = 0
        for obiect in lista:
            if obiect[4] == locatie:
                suma += obiect[3]

        dict_preturi[locatie] = suma

    return dict_preturi
