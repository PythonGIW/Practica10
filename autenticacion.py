# -*- coding: utf-8 -*-

#
# CABECERA AQUI

import hashlib, random, binascii

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
import onetimepass as otp


PIMIENTA = 'Juanito'

mongoclient = MongoClient()
db = mongoclient['giw']
c = db['users']

"""
@route('/')
def index():
    return template('change_password.tpl')
"""
##############
# APARTADO 1 #
##############

# 
# Explicación detallada del mecanismo escogido para el almacenamiento de c
# contraseñas, explicando razonadamente por qué es seguro

"""Consideramos que es seguro el almacenamiento debido a que las contraseñas no se almacenan directamente en la base de datos,
    Primero las pasamos por el algoritmo sha256 despues las mezclamos con una sal generada aleatoriamente y la volvemos 
    a pasar el sha256, finale mente escogemos una palabra clave para volver a mezclarla con la contraseña y de nuevo volver a
    pasar el sha256."""

@post('/signup')
def signup():
    nickname= request.forms.get('nickname')
    name= request.forms.get('name')
    country= request.forms.get('country')
    email= request.forms.get('email')
    password= request.forms.get('password')
    password2= request.forms.get('password2')

    if (password != password2):
        print 'Las contraseñas no coinciden'
    if (db.users.find_one({"nickname": nickname})):
        print 'El alias de usuario ya existe'

    #Guardar las contraseñas con has sha256 
    #Añadir la sal y volver a aplicar has sha256
    print password.hexdigest()
    sal = dameSal(18)
    password= combinar(password, sal)
    db.users.insert_one({"nickname": nickname, "name": name, "country":country, "email":email, "password":password.hexdigest(), "salt":sal})
    print 'Bienvenido usuario ', name

    



def dameSal( longitud):
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

    p = ""
    p = p.join([choice(valores) for i in range(longitud)])
    return p;
        

@post('/change_password')
def change_password():
    nickname= request.forms.get('nickname')
    old_password= request.forms.get('old_password')
    new_password= request.forms.get('new_password')
    user = db.users.find_one({"nickname": nickname})
    if (user != None):
        sal = user["salt"]
        dbpassword= user["password"]
        shassword= combinar(old_password, sal)
        if(shassword.hexdigest() == dbpassword):           
            new_password= combinar(new_password, sal)
            db.users.update_one({"nickname": nickname}, {"$set":{"password": new_password.hexdigest(), "password2":new_password.hexdigest()}})
        else:
            print "Usuario o contraseña incorrectos(==)"
    else:
        print "Usuario o contraseña incorrectos"


            
def combinar(password, sal):
    password = hashlib.sha256(password)
    password= hashlib.sha256(password.hexdigest() + sal)
    #Concatenar la pimienta y volver a hacer sha256
    password= password.hexdigest() + PIMIENTA
    return hashlib.sha256(password)


@post('/login')
def login():
    nickname= request.forms.get('nickname')
    password= request.forms.get('password')
    user = db.users.find_one({"nickname": nickname})
    if(user != None):
        sal = user["salt"]
        dbpassword= user["password"]
        shassword= combinar(password, sal)
        print dbpassword
        print shassword
        if(shassword.hexdigest() == dbpassword):
            print "Bienvenido: " + user["name"]
        else: 
            print "Usuario o contraseña incorrectos(==)"
    else: 
        print "Usuario o contraseña incorrectos"





##############
# APARTADO 2 #
##############
  

def gen_secret():
    # >>> gen_secret()
    # '7ZVVBSKR22ATNU26'
    valores = "234567ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    p = ""
    p = p.join([choice(valores) for i in range(16)])
    return p;
    
    
def gen_gauth_url(app_name, username, secret):
    # >>> gen_gauth_url( 'GIW_grupoX', 'pepe_lopez', 'JBSWY3DPEHPK3PXP')
    # 'otpauth://totp/pepe_lopez?secret=JBSWY3DPEHPK3PXP&issuer=GIW_grupoX
    return "otpauth://totp/" + username + "?secret=" + secret + "&issuer=" + app_name
        

def gen_qrcode_url(gauth_url):
    # >>> gen_qrcode_url('otpauth://totp/pepe_lopez?secret=JBSWY3DPEHPK3PXP&issuer=GIW_grupoX')
    # 'http://api.qrserver.com/v1/create-qr-code/?data=otpauth%3A%2F%2Ftotp%2Fpepe_lopez%3Fsecret%3DJBSWY3DPEHPK3PXP%26issuer%3DGIW_grupoX'
    return "https://api.qrserver.com/v1/create-qr-code/?data="+gauth_url  


@post('/signup_totp')
def signup_totp():
    nickname= request.forms.get('nickname')
    name= request.forms.get('name')
    country= request.forms.get('country')
    email= request.forms.get('email')
    password= request.forms.get('password')
    password2= request.forms.get('password2')

    if (password != password2):
        return template("error_totp.tpl", username = nickname) #FALTAAAAAAAAAAAAAAA tpl
    if (db.users.find_one({"nickname": nickname})):
        return template("error_user_totp.tpl", username = nickname)

    #Guardar las contraseñas con has sha256 
    #Añadir la sal y volver a aplicar has sha256
    sal = dameSal(18)
    password= combinar(password, sal)
    semilla = gen_secret()
    db.users.insert_one({"nickname": nickname, "name": name, "country":country, "email":email, "password":password.hexdigest(), "salt":sal, "semilla":semilla})
    
    #GENERAS LA SEMILLA Y LAS GUARDAS EN LA BASE DE DATOS (UPDATE)
    qr = gen_qrcode_url(gen_gauth_url("myProyect", nickname, semilla));
    return template("bienvenida_totp.tpl", username = nickname, semilla= semilla, qr = qr) 
        
        
@post('/login_totp')        
def login_totp():
    nickname= request.forms.get('nickname')
    password= request.forms.get('password')
    totp= request.forms.get('totp')
    user = db.users.find_one({"nickname": nickname})
    if(user != None):
        sal = user["salt"]
        dbpassword= user["password"]
        shassword= combinar(password, sal)
        if(shassword.hexdigest() == dbpassword):
            totp2 = otp.get_totp(user['semilla'])
            if(otp.valid_toptp(toptp,resul["secret"])):
                return "Bienvenido "+ user["name"]
            print "Bienvenido: " + user["name"]
        else: 
            print "Usuario o contraseña incorrectos"
    else: 
        print "Usuario o contraseña incorrectos"


    
if __name__ == "__main__":
    # NO MODIFICAR LOS PARÁMETROS DE run()
    run(host='localhost',port=8080,debug=True)


"""
Ejemplo para hacer insert y update en pymongo

db.users.insert_one({"_id": _id, "name": name, "country":country, "email":email, "password":new_pass, "password2":passw2, "salt":salt})
db.users.update_one({"_id":_id}, {"$set":{"password": new_pass, "password2":new_pass}

"""