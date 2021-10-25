from Tests.testCRUD import testAdaugaObiect, testStergeObiect
from Tests.testDomain import test_obiect
from Tests.testFunctionalitati import testSchimbareLocatie, testConcatenare, testPretMaxim


def runAllTests():
    test_obiect()
    testAdaugaObiect()
    testStergeObiect()
    testSchimbareLocatie()
    testConcatenare()
    testPretMaxim()
