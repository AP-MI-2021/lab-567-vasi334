from Domain.obiect import creeaza_obiect, getID


def adauga_obiect(ID, nume, descriere, pret_achizitie, locatie, lista):
    """
    Adauga un obiect intr-o lista
    :param ID: str
    :param nume: str
    :param descriere: str
    :param pret_achizitie: float
    :param locatie: str
    :return: O lista reprezentand atat elementele vechi, cat si noul obiect
    """
    if getByID(ID, lista) is not None:
        raise ValueError('ID-ul exista deja!')
    if pret_achizitie < 0:
        raise ValueError('Pretul trebuie sa fie mai mare decat 0 (zero).')
    if nume == '':
        raise ValueError('Numele trebuie sa contina minim un caracter.')
    obiect = creeaza_obiect(ID, nume, descriere, pret_achizitie, locatie)

    return lista + [obiect]


def getByID(ID, lista):
    for obiect in lista:
        if getID(obiect) == ID:
            return obiect

    return None


def sterge_obiect(ID, lista):
    if getByID(ID, lista) is None:
        raise ValueError('Nu exista un obiect cu ID-ul dat!')
    return [obiect for obiect in lista if getID(obiect) != ID]


def modificareObiect(ID, nume, descriere, pret_achizitie, locatie, lista):
    if getByID(ID, lista) is None:
        raise ValueError('Nu exista un obiect cu ID-ul dat!')
    if pret_achizitie < 0:
        raise ValueError('Pretul trebuie sa fie mai mare decat 0 (zero).')
    if nume == '':
        raise ValueError('Numele trebuie sa contina minim un caracter.')
    list_noua = []
    for obiect in lista:
        if getID(obiect) == ID:
            obiect_nou = creeaza_obiect(ID, nume, descriere, pret_achizitie, locatie)
            list_noua.append(obiect_nou)
        else:
            list_noua.append(obiect)

    return list_noua
