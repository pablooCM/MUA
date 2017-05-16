import sqlite3
import smtplib
import telnetlib
import sys
import urllib
import urllib2

def verificarDatos(usuario, contrasenna):
    conexion = sqlite3.connect("correo.db")
    c = conexion.cursor()
    c.execute("SELECT * FROM usuario")
    data = c.fetchall()
    print (len(data))
    i = 0
    informacion = ""
    while(i < len(data)):
        if(data[i][0] == usuario and data[i][1] == contrasenna):
            informacion = "Datos validos"
        i = i + 1
    return informacion

def enviarCorreo(destino, asunto, mensaje, correoOrigen):
    print("entramos aqui")
    print(mensaje)
    datos = '"'+mensaje+'"'
    print ("esto lo hace")
    tn = telnetlib.Telnet("192.168.43.62","25")
    server = smtplib.SMTP(tn.host)
    server.set_debuglevel(1)
    print("el mensaje aqui es "+ datos)
    print (type("hola todo"))
    server.sendmail('"'+correoOrigen+'"', '"'+destino+'"',datos)
    server.quit()

def prueba():
    url = "http://localhost:8080/inicioSesion"
    data = urllib.urlencode({'email':"email","contrasenna":"contrasenna"})
    print("----------------------------")
    print(data)
    req = urllib2.Request(url,data)
    response = urllib2.urlopen(req)
    d = response.read()
    print("ESTO SON LOS DATOS")
    print (d)
