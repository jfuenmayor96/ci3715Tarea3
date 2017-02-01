'''
Created on Jan 31, 2017

@author: Julio Fuenmayor 13-10488
@author: Gianni Manilia 12-10903
'''

class BilleteraElectronica():

    def __init__(self, identificador = None, nombre = None, apellido = None, ci = None, pin = None):
                
        self.identificador = identificador
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        self.pin = pin
        
        # Utilizar objetos del tipo Transaccion para llenar los siguiente atributos
        self.saldoAcumulado = 0  #Ir actualizando esto a medida que se use la funcion recargar
        self.recargas = []
        self.consumos = []
        
    # Metodos de validacion de atributos
    
    def validName(self):
        if self.nombre.isalpha() and self.nombre is not None:
            return True
        else: 
            return False
     
    def validSurname(self):
        if self.apellido.isalpha() and self.apellido is not None:
            return True
        else: 
            return False
        
    def validID(self):
        if isinstance(self.ci, int) and self.ci > -1 and self.ci is not None: 
            return True
        else:
            return False
        
    def validIdentifier(self):
        if isinstance(self.identificador, int) and self.identificador > -1 and self.identificador is not None:
            return True
        else: 
            return False
        
    def validPin(self):
        if isinstance(self.pin, int) and self.pin is not None:
            return True
        else: 
            return False
        
    # Operaciones financieras
    
    def saldo(self):
        return self.saldoAcumulado
    
    def recargar(self, recarga):
        if (recarga.monto < 0 ):
            return "Monto de recarga invalido"
        else:
            self.recargas.append(recarga)
            self.saldoAcumulado += recarga.monto
    
    def consumo(self, transaccion):
        if (transaccion.pin != self.pin):
            return "PIN invalido"
        elif (self.saldoAcumulado < transaccion.monto):
            return "Saldo insuficiente"
        else:
            self.consumos.append(transaccion)
            self.saldoAcumulado -= transaccion.monto
            
            
    