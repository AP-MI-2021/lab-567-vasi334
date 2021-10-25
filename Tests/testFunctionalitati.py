from Domain.obiect import getLocatie, getDescriere
from Logic.CRUD import adauga_obiect, getByID
from Logic.Functionalitati import mutare_locatie, concatenare_string, determinare_pret


def testSchimbareLocatie():
    lista = []
    lista = adauga_obiect('1', 'suc', 'Cola', 4.6, 'rai2', lista)
    lista = adauga_obiect('2', 'apa', 'Dorna', 3.5, 'rai3', lista)
    lista = adauga_obiect('3', 'ciocolata', 'Milka', 4.0, 'rai5', lista)

    lista = mutare_locatie('rai7', lista)

    assert getLocatie(getByID('1', lista)) == 'rai7'
    assert getLocatie(getByID('2', lista)) == 'rai7'
    assert getLocatie(getByID('3', lista)) == 'rai7'


def testConcatenare():
    lista = []
    lista = adauga_obiect('1', 'suc', 'Cola', 4.6, 'rai2', lista)
    lista = adauga_obiect('2', 'apa', 'Dorna', 3.5, 'rai3', lista)
    lista = adauga_obiect('3', 'ciocolata', 'Milka', 4.0, 'rai5', lista)

    lista = concatenare_string(3.7, ' bun', lista)

    assert getDescriere(getByID('1', lista)) == 'Cola bun'
    assert getDescriere(getByID('2', lista)) == 'Dorna'
    assert getDescriere(getByID('3', lista)) == 'Milka bun'


def testPretMaxim():
    lista = []
    lista = adauga_obiect('1', 'suc', 'Cola', 4.6, 'rai2', lista)
    lista = adauga_obiect('2', 'apa', 'Dorna', 3.5, 'rai3', lista)
    lista = adauga_obiect('3', 'ciocolata', 'Milka', 4.0, 'rai3', lista)

    assert determinare_pret(lista) == {'rai2': 4.6, 'rai3': 4.0}
