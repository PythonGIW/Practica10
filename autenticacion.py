# -*- coding: utf-8 -*-

#
# CABECERA AQUI

import hashlib, random

"""
Autores: 
Alberto Marquez
Álvaro Asenjo
Juan Jose Montiel 
Declaramos que esta solución
es fruto exclusivamente de nuestro trabajo personal. No hemos sido
ayudados por ninguna otra persona ni hemos obtenido la solución de
fuentes externas, y tampoco hemos compartido nuestra solución con
nadie. Declaramos además que no hemos realizado de manera desho-
nesta ninguna otra actividad que pueda mejorar nuestros resultados
ni perjudicar los resultados de los demás.

"""

# Resto de importaciones
from bottle import route, request, response, run, template, error, post
from random import choice
from pymongo import MongoClient


PIMIENTA = 'Juanito'

mongoclient = MongoClient()
db = mongoclient['giw']
c = db['users']

##############
# APARTADO 1 #
##############

# 
# Explicación detallada del mecanismo escogido para el almacenamiento de c
# contraseñas, explicando razonadamente por qué es seguro
#

@post('/signup')
def signup():
    nickname= request.forms.get('nickname')
    name= request.forms.get('name')
    country= request.forms.get('country')
    email= request.forms.get('email')
    password= request.forms.get('password')
    password2= request.forms.get('password2')

    if (password != password2):
    #print('Las contraseñas no coinciden')
    if (db.users.find_one({"nickname": nickname})):
    #print('El alias de usuario ya existe')

    #Guardar las contraseñas con has sha256 
    password = hashlib.sha256(password)
    #Añadir la sal y volver a aplicar has sha256 
    sal = dameSal(len(password))
    password= hashlib.sha256(password + sal)
    #Concatenar la pimienta y volver a hacer sha256
    password= password + PIMIENTA
    password = hashlib.sha256(password)
    db.users.insert_one({"nickname": nickname, "name": name, "country":country, "email":email, "password":password, "salt":sal})
    #print ('Bienvenido usuario ' + name)

    



def dameSal(int longitud):
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

    p = ""
    p = p.join([choice(valores) for i in range(longitud)])
    return p;
        

@post('/change_password')
def change_password():
    nickname= request.forms.get('nickname')
    old_password= request.forms.get('old_password')
    new_password= request.forms.get('new_password')
    user = db.users.find_one({"nickname": nickname, "password":old_password, "salt":sal})
    if (user != None):
        oldPassword= hashlib.sha256(oldPassword + sal)
        if()

            

@post('/login')
def login():
    nickname= request.forms.get('nickname')
    password= request.forms.get('password')
    user = db.users.find_one({"nickname": nickname, "name": name, "password":password, "salt":sal})
    if(user != None):
        sal = user["salt"]
        dbpassword = user["password"]
        shassword= hashlib.sha256(oldPassword + sal)
        if(shassword == dbpassword)
            print "Bienvenido" + user["name"]
    else: 
        print "Usuario o contraseña incorrectos"





##############
# APARTADO 2 #
##############


def gen_secret():
    # >>> gen_secret()
    # '7ZVVBSKR22ATNU26'
    pass
    
    
def gen_gauth_url(app_name, username, secret):
    # >>> gen_gauth_url( 'GIW_grupoX', 'pepe_lopez', 'JBSWY3DPEHPK3PXP')
    # 'otpauth://totp/pepe_lopez?secret=JBSWY3DPEHPK3PXP&issuer=GIW_grupoX
    pass
        

def gen_qrcode_url(gauth_url):
    # >>> gen_qrcode_url('otpauth://totp/pepe_lopez?secret=JBSWY3DPEHPK3PXP&issuer=GIW_grupoX')
    # 'http://api.qrserver.com/v1/create-qr-code/?data=otpauth%3A%2F%2Ftotp%2Fpepe_lopez%3Fsecret%3DJBSWY3DPEHPK3PXP%26issuer%3DGIW_grupoX'
    pass
    


@post('/signup_totp')
def signup_totp():
    pass
        
        
@post('/login_totp')        
def login_totp():
    pass

    
if __name__ == "__main__":
    # NO MODIFICAR LOS PARÁMETROS DE run()
    run(host='localhost',port=8080,debug=True)


"""
Ejemplo para hacer insert y update en pymongo

db.users.insert_one({"_id": _id, "name": name, "country":country, "email":email, "password":new_pass, "password2":passw2, "salt":salt})
db.users.update_one({"_id":_id}, {"$set":{"password": new_pass, "password2":new_pass}

"""