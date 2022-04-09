from config.database import db

def iansertrRegistro(nombre,descripcion,imagen,celular,direccion,correo,contraseña):
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

