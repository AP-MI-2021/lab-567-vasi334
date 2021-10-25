from Domain.obiect import getID, getNume, getDescriere, getPretAchizitie, getLocatie
from Logic.CRUD import adauga_obiect, getByID, sterge_obiect, modificareObiect


def testAdaugaObiect():
    lista = []
    lista = adauga_obiect('1', 'suc', 'Cola', 4.50, 'raft', lista)

    assert getID(getByID('1', lista)) == '1'
    assert getNume(getByID('1', lista)) == 'suc'
    assert getDescriere(getByID('1', lista)) == 'Cola'
    assert getPretAchizitie(getByID('1', lista)) == 4.50
    assert getLocatie(getByID('1', lista)) == 'raft'


def testStergeObiect():
    lista = []
    lista = adauga_obiect('1', 'suc', 'Cola', 4.50, 'raf1', lista)
    lista = adauga_obiect('2', 'apa', 'Dorna', 2.50, 'raf2', lista)

    lista = sterge_obiect('1', lista)

    assert len(lista) == 1
    assert getByID('1', lista) is None
    assert getByID('2', lista) is not None

    lista = sterge_obiect('3', lista)

    assert len(lista) == 1
    assert getByID('2', lista) is not None


def testModificaObiect():
    lista = []
    lista = adauga_obiect('1', 'suc', 'Cola', 4.50, 'raf1', lista)
    lista = adauga_obiect('2', 'apa', 'Dorna', 2.50, 'raf2', lista)
    lista = modificareObiect('1', 'paine', 'Neagra', 2.5, 'raf2', lista)

    obiect_modificat = getByID('1', lista)
    assert getID(obiect_modificat) == '1'
    assert getNume(obiect_modificat) == 'paine'
    assert getDescriere(obiect_modificat) == 'Neagra'
    assert getPretAchizitie(obiect_modificat) == 2.5
    assert getLocatie(obiect_modificat) == 'raf2'

    obiect_nemodificat = getByID('2', lista)
    assert getID(obiect_nemodificat) == '2'
    assert getNume(obiect_nemodificat) == 'apa'
    assert getDescriere(obiect_nemodificat) == 'Dorna'
    assert getPretAchizitie(obiect_nemodificat) == 2.5
    assert getLocatie(obiect_nemodificat) == 'raf2'
