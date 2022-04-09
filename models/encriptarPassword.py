import hashlib



def encriptar(contraseña):
   contraseña = hashlib.sha1(contraseña.encode()).hexdigest()
   return contraseña
   
