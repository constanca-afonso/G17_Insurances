# -*- coding: utf-8 -*-
"""
@author: Mariana Marques
(2021)
#objective: Test classes based on generic class Gclass

"""""
db = 'sqlclassestabela.db'
      

# # #Uncomment to test class Cliente (select next 4 lines and press ctrl-1) 
# from classes.cliente import Cliente
# test_class = Cliente
# ob = '100;Antonio Silva;1966-03-12;4000.0'



# # #Uncomment to test class Agente (select next two lines and press ctrl-1) 
# from classes.agente import Agente
# test_class = Agente
# ob = '600;Xavier;Braga'

# #Uncomment to test class Tipo_Apolice (select next two lines and press ctrl-1) 
# from classes.tipo_apolice import Tipo_Apolice
# test_class = Tipo_Apolice
# ob = '600;Saude'

# #Uncomment to test class Apolice
# from classes.apolice import Apolice
# from classes.agente import Agente
# from classes.tipo_apolice import Tipo_Apolice
# Agente.read('data/sqlclassestabela.db')
# Tipo_Apolice.read('data/sqlclassestabela.db')
# Apolice.read('data/sqlclassestabela.db')
# test_class = Apolice
# ob='0;1;1;1;1'

# #Uncomment to test class Apolice_Cliente
# from classes.tipo_apolice import Tipo_Apolice
# from classes.agente import Agente
# from classes.cliente import Cliente
# from classes.apolice import Apolice
# from classes.apolice_cliente import Apolice_Cliente
# Tipo_Apolice.read('data/sqlclassestabela.db')
# Agente.read('data/sqlclassestabela.db')
# Cliente.read('data/sqlclassestabela.db')
# Apolice.read('data/sqlclassestabela.db')
# Apolice_Cliente.read('data/sqlclassestabela.db')
# test_class = Apolice_Cliente
# ob='1;1;1;11/11/2022;ativo'



import datetime

#Reads the test_class.csv file
test_class.read('data/' + db)

op = ''
while op != 'q':
    print('')
    print('Choose one letter for select the option')
    print('---------------')
    print('l - list')
    print('b - beginning')
    print('n - next')
    print('p - previous')
    print('e - end')
    print('---------------')
    print('i - insert')
    print('m - modify')
    print('r - remove')
    print('---------------')
    print('s - sort by attribute')
    print('f - find by attribute')
    print('---------------')
    print('q - quit')
    print('---------------')
    p = test_class.current()
    print(f'\n{p}')
    op = input('?')
    if op == 'b':
        test_class.first()
    elif op == 'n':
        test_class.nextrec()
    elif op == 'p':
        test_class.previous()
    elif op == 'e':
        test_class.last()
    elif op == 'i':
        p1 = None
        if len(test_class.lst) == 0:
            p = eval('test_class.from_string("' + ob + '")')
            p1 = p
        str_list = list(p.__dict__.keys())
        attrib = str_list[0]
        atype = type(getattr(p, attrib))
        print('leave blank to auto-increment')
        id = input(f'{attrib[1:]} = ')
        if id == "":
            id = 0
        else:
            id = int(id)
        strarg = f'test_class({id}'
        for i in range(1, len(str_list)):
            attrib = str_list[i]
            atype = type(getattr(p, attrib))
            if atype == datetime.date or atype == str:
                value = input(f'{attrib[1:]} = ')
                strarg += f',"{value}"'
            else:
                value = atype(input(f'{attrib[1:]} = '))
                strarg += f',{value}'
        strarg += ')'
        if p1 != None:
            # test_class.lst = list()
            test_class.remove(getattr(p, str_list[0]))
        print(strarg)
        pobj = eval(strarg)
        attrib = str_list[0]
        code = getattr(pobj, attrib)
        obj=test_class.current(code)
        test_class.insert(code)

    elif op == 'm':
        str_list = list(p.__dict__.keys())
        attrib = str_list[0]
        id = input(f'Record {attrib[1:]} = ') 
        if id != "":
            id = int(id)
            obj=test_class.current(id)
            print('Leave blank or new value to modify')
            for attrib in str_list[1:]:
                # attrib = str_list[i]
                value = input(f'{attrib[1:]} = ') 
                if value != "":
                    atype = type(getattr(p, attrib))
                    if atype == datetime.date:
                        setattr(obj, attrib, datetime.date.fromisoformat(value))
                    else:
                        setattr(obj, attrib, atype(value))
        # id = getattr(obj, test_class.att[0][1:])
        test_class.update(id)
    elif op == 'r':
        str_list = list(p.__dict__.keys())
        attrib = str_list[0]
        atype = type(getattr(p, attrib))
        cod = atype(input(f'{attrib[1:]} = '))
        if cod in test_class.lst:
            print(test_class.obj[cod])
            print('Confirm that you want to delete the record (y/n)?', end='')
            if input().upper() == 'Y':
                test_class.remove(cod)
    elif op == 'l':
        for code in test_class.lst:
            print(test_class.obj[code])
    elif op == 's':
        # Sort products by attribute in ascending order
        attrib = input('sort by attribute name:')
        if '_' + attrib in list(p.__dict__.keys()):
            reverse = False
            if input('Reverse (False):'):
                reverse = True
            codep = p.id         # Keep the position
            test_class.sort(attrib, reverse)
            for code in test_class.lst:
                print(test_class.obj[code])
            test_class.current(codep)
    elif op == 'f':
        # Find objects with a given value in an attribute
        attrib = input('Attribute name:')
        if '_' + attrib in list(p.__dict__.keys()):
            atype = type(getattr(p, attrib))
            value = atype(input('Value:'))
            fobjs = test_class.find(value, attrib)
            if len(fobjs) > 0:
                test_class.current(fobjs[0].id)
                for obj in fobjs:
                    print(obj)

