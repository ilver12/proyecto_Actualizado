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

def crearProducto(nombre,descripcion,precio,estado,imagen, usuario_id):
    cursor = db.cursor()
    cursor.execute("insert into productos(nombre,descripcion,precio,estado,imagen,usuario_id) values(%s,%s,%s,%s,%s,%s)",(
        nombre,
        descripcion,
        precio,
        estado,
        imagen,
        usuario_id,

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

def actualizarRegistro(nombre,descripcion,celular,direccion,correo,contraseña, imagen, id):
    cursor = db.cursor()
    cursor.execute("UPDATE usuarios SET  nombre = %s, descripcion = %s, celular = %s, direccion = %s, correo = %s, contraseña = %s , imagen =%s  WHERE id = %s", 
        (nombre, 
        descripcion,
        celular,
        direccion,
        correo,
        contraseña,
        imagen,
        id,
        )) 
    
    cursor.close()

def obtenerProductos(usuario_id):
    cursor = db.cursor(dictionary = True)
    cursor.execute("select * from productos where usuario_id =%s ",(usuario_id,))
    productos = cursor.fetchall() #obtener todo
    #producto = cursor.fetchone()
    print(productos)
    cursor.close()
    return productos

def mostrarRegistro():
    cursor = db.cursor(dictionary = True)
    cursor.execute("select * from usuarios")
    usuarios = cursor.fetchall() #obtener todo
    #producto = cursor.fetchone()
    print(usuarios)
    cursor.close()
    return usuarios

def actualizarPass(correo,contraseñaN):
    cursor = db.cursor()
    cursor.execute("UPDATE usuarios SET contraseña='"+contraseñaN+"' where correo='"+correo+"'")
    cursor.close()
