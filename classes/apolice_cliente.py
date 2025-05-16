# @author: Mariana Marques
# @objective: class Apolice_Cliente

# Class Apolice_Cliente
import datetime
from classes.apolice import Apolice
from classes.cliente import Cliente


# Import the generic class
from classes.gclass import Gclass

class Apolice_Cliente(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier attribute 'id' must be the first on the list
    att = ['_id','_id_Apolice','_id_Cliente','_data_efetiva','_estado']
    # Class header title
    header = 'Apolice_Cliente'
    # field description for use in, for example, input form
    des = ['_id','_id_Apolice','_id_Cliente','_data_efetiva','_estado']

    # Constructor: Called when an object is instantiated
    def __init__(self, id, id_Apolice, id_Cliente, data_efetiva, estado):
        super().__init__()
        # Object attributes
        # Check the customer referential integrity
        id_Cliente = int(id_Cliente)
        id_Apolice = int(id_Apolice)
        if id_Cliente in Cliente.lst:
            if id_Apolice in Apolice.lst:
                id = Apolice_Cliente.get_id(id)
                self._id = id
                self._id_Apolice = id_Apolice
                self._id_Cliente = id_Cliente
                self._data_efetiva = datetime.datetime.strptime(data_efetiva, "%Y/%m/%d").date()
                self._estado = estado
                # Add the new object to the Order List
                Apolice_Cliente.obj[id] = self
                Apolice_Cliente.lst.append(id)
            else:
                print('Apolice ', id_Apolice, ' not found')
        else:
            print('Cliente ', id_Cliente, ' not found')

    # Object properties
    # code property getter method
    @property
    def id(self):
        return self._id

    # agente property getter method
    @property
    def id_Cliente(self):
        return self._id_Cliente

    # agente property setter method
    @id_Cliente.setter
    def id_Cliente(self, id_Cliente):
        if id_Cliente in Cliente.lst:
            self._id_Cliente = id_Cliente
        else:
            print('Cliente ', id_Cliente, ' not found')
            
    # apolice property getter method
    @property
    def id_Apolice(self):
        return self._id_Apolice
    
    # apolice property setter method
    @id_Apolice.setter
    def id_Apolice(self, id_Apolice):
        if id_Apolice in Apolice.lst:
            self._id_Apolice = id_Apolice
        else:
            print('Apolice ', id_Apolice, ' not found')
            
    @property
    def data_efetiva(self):
        return self._data_efetiva
    @data_efetiva.setter
    def data_efetiva(self, data_efetiva):
        self._data_efetiva = data_efetiva
    # estado property getter method
    @property
    def estado(self):
        return self._estado
    # estado property setter method
    @estado.setter
    def estado(self, estado):
        self._estado = estado
