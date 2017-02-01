'''
Created on Jan 31, 2017

@author: Julio Fuenmayor 13-10488
@author: Gianni Manilia 12-10903

'''
import unittest
import datetime
from BilleteraElectronica import *
from Recarga import *
from Transaccion import *


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
    
    #Caso frontera    
    def testSaldoCero(self):
        self.assertEquals(0, self.billetera.saldo())
        
    #Caso esquina
    def testRecargaEsquina1(self):
        recarga = Recarga(1, datetime.datetime.today())
        self.billetera.recargar(recarga)
        self.assertEquals(1, self.billetera.saldo())

    #Caso frontera
    def testRecargaFrontera(self):
        recarga = Recarga(float('inf'), datetime.datetime.today())
        self.billetera.recargar(recarga)
        self.assertEquals(float('inf'), self.billetera.saldo())
    
    #Caso esquina
    def testRecargaEsquina2(self):
        recarga = Recarga(float('inf')-1, datetime.datetime.today())
        self.billetera.recargar(recarga)
        self.assertEquals(float('inf')-1, self.billetera.saldo())
    
    #Caso interior            
    def testRecargaPositiva(self):
        recarga = Recarga(1000,datetime.datetime.today())
        self.billetera.recargar(recarga)
        self.assertEquals(1000, self.billetera.saldo())
        
    #Caso malicioso
    def testRecargaNegativa(self):
        recarga = Recarga(-10,datetime.datetime.today())
        self.billetera.recargar(recarga)
        self.assertEquals("Monto de recarga invalido", self.billetera.recargar(recarga))
        
    #Caso malicioso        
    def testConsumoPinInvalido(self):
        recarga = Recarga(1000,datetime.datetime.today())
        self.billetera.recargar(recarga)
        transaccion = Transaccion(4,500,datetime.datetime.today(),"Bodega")
        self.assertEquals("PIN invalido", self.billetera.consumo(transaccion))
    
    #Caso malicioso
    def testConsumoSaldoInsuficiente(self):
        recarga = Recarga(1000,datetime.datetime.today())
        self.billetera.recargar(recarga)
        transaccion = Transaccion(1111,1001,datetime.datetime.today(),"Bodega")
        self.assertEquals("Saldo insuficiente", self.billetera.consumo(transaccion))
     
    #Caso interior
    def testConsumoValido(self):
        recarga = Recarga(1000,datetime.datetime.today())
        self.billetera.recargar(recarga)
        transaccion = Transaccion(1111,500,datetime.datetime.today(),"Bodega")
        self.billetera.consumo(transaccion)
        self.assertEquals(500, self.billetera.saldo())
        
                  
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()