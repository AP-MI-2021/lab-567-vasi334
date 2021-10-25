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

    return [ID, nume, descriere, pret_achizitie, locatie]


def getID(obiect):
    """
    Da ID-ul unui obiect.
    :param obiect: Dictionar ce contine un obiect.
    :return: ID-ul obiectului
    """
    return obiect[0]


def getNume(obiect):
    return obiect[1]


def getDescriere(obiect):
    return obiect[2]


def getPretAchizitie(obiect):
    return obiect[3]


def getLocatie(obiect):
    return obiect[4]


def toString(obiect):
    return f"ID: {getID(obiect)}\n Nume: {getNume(obiect)}\n " \
           f"Descriere: {getDescriere(obiect)}\n " \
           f"Pret achizitie: {getPretAchizitie(obiect)}\n Locatie: {getLocatie(obiect)}"
