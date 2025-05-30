#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 18:13:08 2025

@author: margaridavigario
"""
from classes.gclass import Gclass
class Agente(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_id','_nome','_regiao']
    # Class header title
    header = 'Agente'
    # field description for use in, for example, input form
    des = ['Id','Nome','Região']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, nome,regiao):
        super().__init__()
        # Object attributes
        id = Agente.get_id(id)
        self._id = id
        self._nome = nome
        self._regiao = regiao
        # Add the new object to the dictionary of objects
        Agente.obj[id] = self
        # Add the id to the list of object ids
        Agente.lst.append(id)
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
    # regiao property getter method
    @property
    def regiao(self):
        return self._regiao
    # regiao property setter method
    @regiao.setter
    def regiao(self, regiao):
        self._regiao = regiao
    