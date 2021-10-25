from Domain.obiect import getLocatie, getDescriere
from Logic.CRUD import adauga_obiect, getByID
from Logic.Functionalitati import mutare_locatie, concatenare_string, determinare_pret


def testSchimbareLocatie():
    lista = []
    lista = adauga_obiect('1', 'suc', 'Cola', 4.6, 'raionul 2', lista)
    lista = adauga_obiect('2', 'apa', 'Dorna', 3.5, 'raionul 3', lista)
    lista = adauga_obiect('3', 'ciocolata', 'Milka', 4.0, 'raionul 5', lista)

    lista = mutare_locatie('raionul 7', lista)

    assert getLocatie(getByID('1', lista)) == 'raionul 7'
    assert getLocatie(getByID('2', lista)) == 'raionul 7'
    assert getLocatie(getByID('3', lista)) == 'raionul 7'


def testConcatenare():
    lista = []
    lista = adauga_obiect('1', 'suc', 'Cola', 4.6, 'raionul 2', lista)
    lista = adauga_obiect('2', 'apa', 'Dorna', 3.5, 'raionul 3', lista)
    lista = adauga_obiect('3', 'ciocolata', 'Milka', 4.0, 'raionul 5', lista)

    lista = concatenare_string(3.7, ' bun', lista)

    assert getDescriere(getByID('1', lista)) == 'Cola bun'
    assert getDescriere(getByID('2', lista)) == 'Dorna'
    assert getDescriere(getByID('3', lista)) == 'Milka bun'


def testPretMaxim():
    lista = []
    lista = adauga_obiect('1', 'suc', 'Cola', 4.6, 'raionul 2', lista)
    lista = adauga_obiect('2', 'apa', 'Dorna', 3.5, 'raionul 3', lista)
    lista = adauga_obiect('3', 'ciocolata', 'Milka', 4.0, 'raionul 3', lista)

    assert determinare_pret(lista) == {'raionul 2': 4.6, 'raionul 3': 4.0}