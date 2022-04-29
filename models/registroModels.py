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

def crearProducto(nombre,descripcion,precio,estado,imagen):
    cursor = db.cursor()
    cursor.execute("insert into productos(Nombre,Descripcion,Precio,Estado,Imagen) values(%s,%s,%s,%s,%s)",(
        nombre,
        descripcion,
        precio,
        estado,
        imagen,

    ))
    cursor.close()

def actualizarProducto(nombre,descripcion,precio,estado,imagen,id):
    cursor = db.cursor()
    cursor.execute("UPDATE productos SET  nombre = %s, descripcion = %s, precio = %s, estado = %s, imagen =%s  WHERE id = %s", 
        (nombre, 
        descripcion,
        precio,
        estado,
        imagen,
        id,
        )) 
    cursor.close()

def obtenerProductos():
    cursor = db.cursor(dictionary = True)
    cursor.execute("select * from productos")
    productos = cursor.fetchall() #obtener todo
    #producto = cursor.fetchone()
    print(productos)
    cursor.close()
    return productos

def actualizarPass(correo,contraseñaN):
    cursor = db.cursor()
    cursor.execute("UPDATE usuarios SET contraseña='"+contraseñaN+"' where correo='"+correo+"'")
    cursor.close()
