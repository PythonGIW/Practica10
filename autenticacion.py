# -*- coding: utf-8 -*-

#
# CABECERA AQUI
#
import hashlib, random


# Resto de importaciones
from bottle import route, request, response, run, template, error, post
from random import choice

PIMIENTA = 'Juanito'
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
    #mostrar que "Las contraseñas no coinciden"

    #Guardar las contraseñas con has sha256 
    password = hashlib.sha256(password)
    #Añadir la sal y volver a aplicar has sha256 
    sal = dameSal(len(password))
    password= hashlib.sha256(password + sal)
    #Concatenar la pimienta y volver a hacer sha256
    password= password + PIMIENTA
    hashlib.sha256(password)

    



def dameSal(int longitud):
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

    p = ""
    p = p.join([choice(valores) for i in range(longitud)])
    return p;
        

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
