'''
Created on Jan 31, 2017

@author: Julio Fuenmayor 13-10488
@author: Gianni Manilia 12-10903

'''
import unittest
from BilleteraElectronica import *


class Test(unittest.TestCase):

    # Se inicializa una instancia de BilleteraElectronica con la cual se van a 
    #realizar los tests unitarios.
    def setUp(self):
        self.billetera = BilleteraElectronica(1,"julio","fuenmayor",24818828)
        
    def testIdentificadorDeInstanciaValida(self):
        assert(self.billetera.validIdentifier()), "Identificador de instancia inválido."
        
    def testNombreValido(self):
        assert(self.billetera.validName()), "Atributo nombre inválido."

    def testApellidoValido(self):
        assert(self.billetera.validSurname()), "Atributo apellido inválido."
        
    def testCIValida(self):
        assert(self.billetera.validID()), "Atributo CI inválido."
        
    
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()