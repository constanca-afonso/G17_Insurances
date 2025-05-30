"""
@author: António Brito / Carlos Bragança
(2025) objective: class Person
"""
# Class Cliente - generic version with inheritance
from classes.gclass import Gclass
import datetime
class Cliente(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_id','_nome','_email','_nivel_risco','_foto']
    # Class header title
    header = 'Cliente'
    # field description for use in, for example, input form
    des = ['Id','Nome','Email','Nível Risco', 'Foto']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, nome, email, nivel_risco,foto):
        super().__init__()
        # Object attributes
        id = Cliente.get_id(id)
        self._id = id
        self._nome = nome
        self._email = email
        self._nivel_risco = nivel_risco
        self._foto=foto
        # Add the new object to the dictionary of objects
        Cliente.obj[id] = self
        # Add the id to the list of object ids
        Cliente.lst.append(id)
    # id property getter method
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id
    # nome property getter method
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    # email property getter method
    @property
    def email(self):
        return self._email
    # email property setter method
    @email.setter
    def email(self, email):
        self._email = email
    # nivel_risco property getter method
    @property
    def nivel_risco(self):
        return self._nivel_risco
    # nivel_risco property setter method
    @nivel_risco.setter
    def nivel_risco(self, nivel_risco):
        self._nivel_risco = nivel_risco
    @property
    def foto(self):
        return self._foto
    @foto.setter
    def foto(self, foto):
        self._foto = foto
        
