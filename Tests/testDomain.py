from Domain.obiect import creeaza_obiect, getID, getNume, getLocatie, getDescriere, getPretAchizitie

def test_obiect():
    obiect = creeaza_obiect('1', 'suc', 'Cola', 4.50, 'raftul 1')

    assert getID(obiect) == '1'
    assert getNume(obiect) == 'suc'
    assert getDescriere(obiect) == 'Cola'
    assert getPretAchizitie(obiect) == 4.50
    assert getLocatie(obiect) == 'raftul 1'
