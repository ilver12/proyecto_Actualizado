from config.database import db

def insertarRegistro(nombre,descripcion,imagen,celular,direccion,correo,contraseña):
    cursor = db.cursor()
    cursor.execute("insert into usuarios(nombre,descripcion,imagen,celular,direccion,correo,contraseña) values(%s,%s,%s,%s,%s,%s,%s)",(
        nombre,
        descripcion,
        imagen,
        celular,
        direccion,
        correo,
        contraseña,
    ))
    cursor.close()

def actualizarPass(correo,contraseñaN):
    cursor = db.cursor()
    cursor.execute("UPDATE usuarios SET contraseña='"+contraseñaN+"' where correo='"+correo+"'")
    cursor.close()
