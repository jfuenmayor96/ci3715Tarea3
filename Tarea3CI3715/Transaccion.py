'''
Created on Jan 31, 2017

@author: Julio Fuenmayor 13-10488
@author: Gianni Manilia 12-10903
'''

class Transacción(object):

    # El argumento fecha debe ser de tipo date
    def __init__(self, monto, fecha, establecimiento):
        self.monto = monto
        self.fecha = fecha
        self.establecimiento = establecimiento
        
        
    
        