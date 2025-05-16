#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 18:15:04 2025

@author: constancaafonso
"""

# Class Tipo_Apolice - generic version with inheritance

from classes.gclass import Gclass
import datetime

class Tipo_Apolice(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_id','_designacao']
    # Class header title
    header = 'Tipo_Apolice'
    # field description for use in, for example, input form
    des = ['Id','Designação']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, designacao):
        super().__init__()
        # Object attributes
        id = Tipo_Apolice.get_id(id)
        self._id = id
        self._designacao = designacao
        # Add the new object to the dictionary of objects
        Tipo_Apolice.obj[id] = self
        # Add the id to the list of object ids
        Tipo_Apolice.lst.append(id)
    # id property getter method
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id
    # designacao property getter method
    @property
    def designacao(self):
        return self._designacao
    @designacao.setter
    def designacao(self, designacao):
        self._designacao = designacao
    