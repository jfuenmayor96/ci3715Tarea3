'''
Created on Jan 31, 2017

@author: Julio Fuenmayor 13-10488
@author: Gianni Manilia 12-10903

'''
import unittest
import datetime
from BilleteraElectronica import *
from Recarga import *


class Test(unittest.TestCase):

    # Se inicializa una instancia de BilleteraElectronica con la cual se van a 
    #realizar los tests unitarios.
    def setUp(self):
        self.billetera = BilleteraElectronica(1,"julio","fuenmayor",24818828,1111)
        
    def testIdentificadorDeInstanciaValida(self):
        assert(self.billetera.validIdentifier()), "Identificador de instancia invalido."
        
    def testNombreValido(self):
        assert(self.billetera.validName()), "Atributo nombre invalido."

    def testApellidoValido(self):
        assert(self.billetera.validSurname()), "Atributo apellido invalido."
        
    def testCIValida(self):
        assert(self.billetera.validID()), "Atributo CI invalido."
        
    def testPinValido(self):
        assert(self.billetera.validPin()), "Atributo PIN invalido."
        
    def testSaldoCero(self):
        self.assertEquals(0, self.billetera.saldo())
    
    def testRecargaNegativa(self):
        recarga = Recarga(-10,datetime.datetime.today())
        self.billetera.recargar(recarga)
        self.assertEquals("Monto de recarga invalido", self.billetera.recargar(recarga))
            
    def testRecargaPositiva(self):
        recarga = Recarga(1000,datetime.datetime.today())
        self.billetera.recargar(recarga)
        self.assertEquals(1000, self.billetera.saldo())
                
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()