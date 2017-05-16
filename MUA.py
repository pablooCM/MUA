import web
import gestor
import os

render = web.template.render('./templates')
global correoOrigen

urls=(
    '/', 'index',
    '/', 'correo',
    '/', 'icorreo',
    '/', 'ecorreo',
    '/','envio',
    '/','inicioSesion',
    '/','iinicioSesion',
    '/index','index',
    '/correo','correo',
    '/icorreo','icorreo',
    '/ecorreo','ecorreo',
    '/envio','envio',
    '/inicioSesion','inicioSesion',
    '/iinicioSesion','iinicioSesion',
    )

app = web.application(urls, globals())

class index:
    def GET(self):
        print ("--------dwoewenbeue")
        
        return render.index()
    def POST(self):
        print ("-------dwoewksu2722727enbeue")
        print ("dwoewenbeue")
        return render.index()

class correo:
    def GET (self):
        print ("-----------------Vamos por aca")
        return render.correo()
    def POST (self):
        print ("----------------eeiwuehuwyegey")
        i = web.input()
        destino = i.email
        asunto = i.subject
        mensaje = (str)(i.message)
        print (type(mensaje))
        global correoOrigen
        print (correoOrigen+" eiejeiie")
        print ("estamos al final")
        if(destino =="" or asunto=="" or mensaje==""):
            print("ingresar todos los datos")
            raise web.seeother('/icorreo')
        else:
            gestor.enviarCorreo(destino, asunto, mensaje, correoOrigen)
            print ("correo enviado")
            raise web.seeother('/ecorreo')

class icorreo:
    def GET (self):
        print ("-----------------Vamos por aca")
        return render.icorreo()
    def POST (self):
        print ("----------------eeiwuehuwyegey")
        i = web.input()
        destino = i.email
        asunto = i.subject
        mensaje = (str)(i.message)
        print (type(mensaje))
        global correoOrigen
        print (correoOrigen+" eiejeiie")
        print ("estamos al final")
        if(destino =="" or asunto=="" or mensaje==""):
            print("ingresar todos los datos")
            raise web.seeother('/icorreo')
        else:
            gestor.enviarCorreo(destino, asunto, mensaje, correoOrigen)
            print ("correo enviado")
            raise web.seeother('/ecorreo')

class ecorreo:
    def GET (self):
        print ("-----------------Vamos por aca")
        return render.ecorreo()
    def POST (self):
        print ("----------------eeiwuehuwyegey")
        i = web.input()
        destino = i.email
        asunto = i.subject
        mensaje = (str)(i.message)
        print (type(mensaje))
        global correoOrigen
        print (correoOrigen+" eiejeiie")
        print ("estamos al final")
        if(destino =="" or asunto=="" or mensaje==""):
            print("ingresar todos los datos")
            raise web.seeother('/icorreo')
        else:
            gestor.enviarCorreo(destino, asunto, mensaje, correoOrigen)
            print ("correo enviado")
            raise web.seeother('/ecorreo')

class inicioSesion():
    def GET (self):
        print("-------dwihewyegw")
        i = web.input()
        return render.inicioSesion()
    def POST(self):
        print ("--------eiwuehwuhewyey")
        i = web.input()
        correo = i.email
        contra = i.contrasenna
        print (correo+" "+contra)
        datos = gestor.verificarDatos(correo, contra)
        if(datos==""):
            print ("datos incorrectos")
            raise web.seeother('/iinicioSesion')
        else:
            print ("BIEEEEEEEEEEN")
            global correoOrigen
            correoOrigen = correo
            raise web.seeother('/correo')

class iinicioSesion():
    def GET (self):
        print("-------dwihewyegw")
        i = web.input()
        return render.iinicioSesion()
    def POST(self):
        print ("--------eiwuehwuhewyey")
        i = web.input()
        correo = i.email
        contra = i.contrasenna
        print (correo+" "+contra)
        datos = gestor.verificarDatos(correo, contra)
        if(datos==""):
            print ("datos incorrectos")
            raise web.seeother('/iinicioSesion')
        else:
            print ("BIEEEEEEEEEEN")
            global correoOrigen
            correoOrigen = correo
            raise web.seeother('/correo')
        

if __name__ == "__main__":
    os.system(" start http://localhost:8080/")
    app.run()
