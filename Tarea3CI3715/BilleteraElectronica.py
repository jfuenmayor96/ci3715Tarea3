'''
Created on Jan 31, 2017

@author: Julio Fuenmayor 13-10488
@author: Gianni Manilia 12-10903
'''

class BilleteraElectronica():

    def __init__(self, identificador = None, nombre = None, apellido = None, ci = None):
                
        self.identificador = identificador
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        
        # Utilizar objetos del tipo Transacción para llenar los siguiente atributos
        self.saldo = 0  #Ir actualizando esto a medida que se use la función recargar
        self.recargas = []
        self.consumos = []
        
    # Métodos de validación de atributos
    
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
        
    # Operaciones financieras
    
    def saldo(self):
        pass
    
    def recargar(self):
        pass
    
    def consumo(self):
        pass 
            
            
    