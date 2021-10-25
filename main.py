from Logic.CRUD import adauga_obiect
from Tests.testAll import runAllTests
from UI.console import runMenu


def main():
    runAllTests()

    lista = []
    lista = adauga_obiect('1', 'suc', 'Cola', 5.6, 'raionul 1', lista)
    lista = adauga_obiect('2', 'apa', 'Borsec', 3.2, 'raionul 2', lista)
    lista = adauga_obiect('3', 'ciocolata', 'Napoca', 3.8, 'raionul 2', lista)

    runMenu(lista)


main()
