'''
Created on Jan 31, 2017

@author: Julio Fuenmayor 13-10488
@author: Gianni Manilia 12-10903

'''
import unittest
from BilleteraElectronica import *



class Test(unittest.TestCase):


    def testIdentificadorDeInstancia(self):
        
        billetera = BilleteraElectronica(1310488)
        
        assert(billetera.identificador is not None), "Usted introdujo un identificador nulo."

    def testDatosDelUsuario(self):
        
        billetera = BilleteraElectronica(1310488, "julio", "fuenmayor", 24818828)        

        assert(billetera.nombre is not None and billetera.apellido is not None and billetera.ci is not None), "Usted introdujo un dato personal erroneo. "

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()