"""
@author: Mariana Marques
(2025) objective: class Apolice
"""
# Class Apolice - generic version with inheritance
from classes.gclass import Gclass
from classes.agente import Agente
from classes.tipo_apolice import Tipo_Apolice

import datetime
class Apolice(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_id','_valor_cobertura','_premio', '_id_Tipo_Apolice', '_id_agente']
    # Class header title
    header = 'Apolice'
    # field description for use in, for example, input form
    des = ['Id','Valor Cobertura', 'Prémio', 'Id Tipo Apólice', 'Id agente']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, valor_cobertura, premio, id_Tipo_Apolice, id_agente):
        super().__init__()
        # Object attributes
        id = Apolice.get_id(id)
        id_agente = int(id_agente)
        id_Tipo_Apolice = int(id_Tipo_Apolice)
        if id_agente in Agente.lst:
            
            if id_Tipo_Apolice in Tipo_Apolice.lst:
                id = Apolice.get_id(id)
                self._id = id
                self._valor_cobertura = float(valor_cobertura)
                self._premio = float(premio)
                self._id_Tipo_Apolice = id_Tipo_Apolice
                self._id_agente = id_agente
                
                # Add the new object to the Order List
                Apolice.obj[id] = self
                Apolice.lst.append(id)
            else:
                print('Tipo_Apolice ', id_Tipo_Apolice, ' not found')
        else:
            print('Agente ', id_agente, ' not found')
       
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id
    
    # valor_cobertura property getter method
    @property
    def valor_cobertura(self):
        return self._valor_cobertura
    # valor_cobertura property setter method
    @valor_cobertura.setter
    def salary(self, valor_cobertura):
        self._valo_cobertura = valor_cobertura
    # premio property getter method
    @property
    def premio(self):
        return self._premio
    # premio property setter method
    @premio.setter
    def premio(self, premio):
        self._premio = premio
     # agente property getter method
    @property
    def id_agente(self):
         return self._id_agente

     # agente property setter method
    @id_agente.setter
    def id_agente(self, id_agente):
         if id_agente in Agente.lst:
             self._id_agente =id_agente
         else:
             print('Agente',id_agente, ' not found')
             
     # apolice property getter method
    @property
    def id_Tipo_Apolice(self):
         return self._id_Tipo_Apolice
     
     # apolice property setter method
    @id_Tipo_Apolice.setter
    def id_Tipo_Apolice(self, id_Tipo_Apolice):
         if id_Tipo_Apolice in Tipo_Apolice.lst:
             self._id_Tipo_Apolice= id_Tipo_Apolice
         else:
             print('Tipo_Apolice ',id_Tipo_Apolice, ' not found')
