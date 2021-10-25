def creeaza_obiect(ID, nume, descriere, pret_achizitie, locatie):
    """
    Creeaza un dictionar ce reprezinta un obiect.
    :param ID: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: float
    :param locatie: string
    :return: un dictionar ce contine un obiect
    """

    return {
        'ID': ID,
        'nume': nume,
        'descriere': descriere,
        'pret_achizitie': pret_achizitie,
        'locatie': locatie
    }


def getID(obiect):
    """
    Da ID-ul unui obiect.
    :param obiect: Dictionar ce contine un obiect.
    :return: ID-ul obiectului
    """
    return obiect['ID']


def getNume(obiect):
    return obiect['nume']


def getDescriere(obiect):
    return obiect['descriere']


def getPretAchizitie(obiect):
    return obiect['pret_achizitie']


def getLocatie(obiect):
    return obiect['locatie']


def toString(obiect):
    return f"ID: {getID(obiect)}\n Nume: {getNume(obiect)}\n " \
           f"Descriere: {getDescriere(obiect)}\n " \
           f"Pret achizitie: {getPretAchizitie(obiect)}\n Locatie: {getLocatie(obiect)}"
