# -*- coding: utf-8 -*-
"""
Created on Mon May 12 14:30:56 2025

@author: maria
"""


from flask import Flask, render_template, request, session

#import das classes 
from classes.userlogin import Userlogin

prev_option = ""


def index(path):
    global prev_option
    butshow, butedit = "enabled", "disabled"
    option = request.args.get("option")
    if option == "edit":
        butshow, butedit = "disabled", "enabled"
    elif option == "delete":
        obj = Userlogin.current()
        Userlogin.remove(obj.id)
        if not Userlogin.previous():
            Userlogin.first()
    elif option == "insert":
        butshow, butedit = "disabled", "enabled"
    elif option == 'cancel':
        pass
    elif prev_option == 'insert' and option == 'save':
        strobj = str(Userlogin.get_id(0))
        strobj = strobj + ';' + request.form["nome"] + ';' + \
        request.form["regiao"] 
        obj = Userlogin.from_string(strobj)
        Userlogin.insert(obj.id)
        Userlogin.last()
    elif prev_option == 'edit' and option == 'save':
        obj = Userlogin.current()
        obj.nome = request.form["nome"]
        obj.regiao = request.form["regiao"]
        Userlogin.update(obj.id)
    elif option == "first":
        Userlogin.first()
    elif option == "previous":
        Userlogin.previous()
    elif option == "next":
        Userlogin.nextrec()
    elif option == "last":
        Userlogin.last()
    elif option == 'exit':
        return "<h1>Thank you for using this app</h1>"
    prev_option = option
    obj = Userlogin.current()
    if option == 'insert' or len(Userlogin.lst) == 0:
        id = 0
        id = Userlogin.get_id(id)
        nome = regiao = ""
    else:
        id = obj.id
        nome = obj.nome
        regiao = obj.regiao
    return render_template("Userlogin.html", butshow=butshow, butedit=butedit, 
                    id=id,nome = nome,regiao=regiao,
                    ulogin=session.get("user"))

