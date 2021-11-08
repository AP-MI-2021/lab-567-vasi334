from Domain.obiect import getID
from Logic.CRUD import adauga_obiect
# start program


def testUndo_Redo():
    undoList = []
    redoList = []
    lista = []

# 1 + 2 + 3 + test (pentru adaugare)
    add = adauga_obiect('4', 'faina', 'alba', 3.3, 'rai1', lista)
    undoList.append(lista)
    lista = add

    add = adauga_obiect('5', 'guma', 'menta', 2.4, 'rai2', lista)
    undoList.append(lista)
    lista = add

    add = adauga_obiect('6', 'suc', 'Santal', 4.8, 'rai1', lista)
    undoList.append(lista)
    lista = add

    assert getID(lista[0]) == "4"
    assert getID(lista[1]) == "5"
    assert getID(lista[2]) == "6"

# 4
    redoList.append(lista)
    lista = undoList.pop()

    assert getID(lista[0]) == "4"
    assert getID(lista[1]) == "5"
    assert len(lista) == 2

# 5
    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getID(lista[0]) == "4"
    assert undoList == [[]]

# 6
    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 0
    assert undoList == []

# 7
    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList
    assert len(lista) == 0
    assert undoList == []

# 8 + test (pentru adaugare)
    add = adauga_obiect("4", "laptop", "HP", 4000, "rai2", lista)
    undoList.append(lista)
    lista = add
    redoList.clear()

    add = adauga_obiect("5", "laptop", "Asus", 3000, "rai1", lista)
    undoList.append(lista)
    lista = add

    add = adauga_obiect("6", "laptop", "Lenovo", 2000, "rai1", lista)
    undoList.append(lista)
    lista = add

    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3

# 9
    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3

# 10
    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 2
    assert getID(lista[0]) == "4"
    assert getID(lista[1]) == "5"

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getID(lista[0]) == "4"
    assert undoList == [[]]

# 11
    undoList.append(lista)
    lista = redoList.pop()
    assert len(lista) == 2
    assert len(undoList) == 2
    assert len(redoList) == 1

# 12
    undoList.append(lista)
    lista = redoList.pop()
    assert len(lista) == 3
    assert len(undoList) == 3
    assert len(redoList) == 0

# 13
    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 2
    assert getID(lista[0]) == "4"
    assert getID(lista[1]) == "5"

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getID(lista[0]) == "4"
    assert undoList == [[]]

# 14
    add = adauga_obiect("7", "popcorn", "Chio", 2.3, "rai1", lista)
    undoList.append(lista)
    lista = add
    redoList.clear()

# 15
    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(undoList) == 2
    assert len(lista) == 2

# 16
    redoList.append(lista)
    lista = undoList.pop()
    assert len(undoList) == 1
    assert len(redoList) == 1
    assert len(lista) == 1

# 17
    redoList.append(lista)
    lista = undoList.pop()
    assert len(undoList) == 0
    assert len(redoList) == 2
    assert len(lista) == 0

# 18
    undoList.append(lista)
    lista = redoList.pop()
    assert len(lista) == 1

    undoList.append(lista)
    lista = redoList.pop()
    assert len(lista) == 2
    assert len(redoList) == 0

# 19
    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(redoList) == 0
    assert len(undoList) == 2
    assert len(lista) == 2
