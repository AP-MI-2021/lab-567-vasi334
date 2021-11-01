from Domain.obiect import getLocatie, getDescriere, getID
from Logic.CRUD import adauga_obiect, getByID
from Logic.Functionalitati import mutare_locatie, concatenare_string, determinare_pret, sortare_dupa_pret, \
    afisarea_sumelor_locatii


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


def testSortare():
    lista = []
    lista = adauga_obiect('1', 'suc', 'Cola', 4.6, 'rai2', lista)
    lista = adauga_obiect('2', 'apa', 'Dorna', 3.5, 'rai3', lista)
    lista = adauga_obiect('3', 'ciocolata', 'Milka', 4.0, 'rai3', lista)
    lista = adauga_obiect('4', 'ciocolata', 'Laura', 2.0, 'rai3', lista)

    lista_ordonata = sortare_dupa_pret(lista)

    assert getID(lista_ordonata[0]) == '4'
    assert getID(lista_ordonata[1]) == '2'
    assert getID(lista_ordonata[2]) == '3'
    assert getID(lista_ordonata[3]) == '1'


def testAfisareDupaLocatie():
    lista = []
    lista = adauga_obiect('1', 'suc', 'Cola', 4.6, 'rai2', lista)
    lista = adauga_obiect('2', 'apa', 'Dorna', 3.5, 'rai3', lista)
    lista = adauga_obiect('3', 'ciocolata', 'Milka', 4.0, 'rai3', lista)
    lista = adauga_obiect('4', 'ciocolata', 'Laura', 2.0, 'rai3', lista)

    assert afisarea_sumelor_locatii(lista) == {'rai2': 4.6, 'rai3': 9.5}