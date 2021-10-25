from Domain.obiect import getID, getNume, getDescriere, getPretAchizitie, getLocatie
from Logic.CRUD import adauga_obiect, getByID, sterge_obiect


def testAdaugaObiect():
    lista = []
    lista = adauga_obiect('1', 'suc', 'Cola', 4.50, 'raftul 1', lista)

    assert getID(getByID('1', lista)) == '1'
    assert getNume(getByID('1', lista)) == 'suc'
    assert getDescriere(getByID('1', lista)) == 'Cola'
    assert getPretAchizitie(getByID('1', lista)) == 4.50
    assert getLocatie(getByID('1', lista)) == 'raftul 1'


def testStergeObiect():
    lista = []
    lista = adauga_obiect('1', 'suc', 'Cola', 4.50, 'raftul 1', lista)
    lista = adauga_obiect('2', 'apa', 'Dorna', 2.50, 'raftul 2', lista)

    lista = sterge_obiect('1', lista)

    assert len(lista) == 1
    assert getByID('1', lista) is None
    assert getByID('2', lista) is not None

    lista = sterge_obiect('3', lista)

    assert len(lista) == 1
    assert getByID('2', lista) is not None
