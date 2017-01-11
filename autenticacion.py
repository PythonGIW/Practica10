# -*- coding: utf-8 -*-

#
# CABECERA AQUI

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

from bottle import run, post
from pymongo import MongoClient

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
    pass
    

@post('/change_password')
def change_password():
    pass
            

@post('/login')
def login():
    pass


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