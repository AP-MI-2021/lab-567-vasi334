from Tests.testCRUD import testAdaugaObiect, testStergeObiect
from Tests.testDomain import test_obiect
from Tests.testFunctionalitati import testSchimbareLocatie, testConcatenare, testPretMaxim, testSortare, \
    testAfisareDupaLocatie
from Tests.testUndoRedo import testUndo_Redo


def runAllTests():
    test_obiect()
    testAdaugaObiect()
    testStergeObiect()
    testSchimbareLocatie()
    testConcatenare()
    testPretMaxim()
    testSortare()
    testAfisareDupaLocatie()
    testUndo_Redo()
