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
        self.assertEqual(billetera.identificador, 1310488, "El identificador de la instancia es incorrecto.")

    def testDatosDelUsuario(self):
        
        billetera = BilleteraElectronica(1310488, "julio", "fuenmayor", 24818828)        

        assert(billetera.nombre is not None and billetera.apellido is not None and billetera.ci is not None), "Usted introdujo un dato personal nulo. "
        self.assertEqual(billetera.nombre, "julio", "El nombre de la instancia es incorrecto.")
        self.assertEqual(billetera.apellido, "fuenmayor", "El apellido de la instancia es incorrecto.")
        self.assertEqual(billetera.ci, 24818828, "La cédula de identidad de la instancia es incorrecto.")
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()