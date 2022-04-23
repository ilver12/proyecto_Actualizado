
from flask import Flask, render_template, url_for, request, redirect, flash, session
from config.database import db
from models import registroModels, validarPassword,encriptarPassword
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from smtplib import SMTP
from email.message import EmailMessage
import hashlib
from config import settings

app = Flask(__name__)
app.secret_key = 'RoXVTv4Ei$2g'
s=URLSafeTimedSerializer('Thisisasecret')

@app.get('/')
def home():
    return render_template('home.html')

@app.route('/registro', methods=['GET', 'POST'])
def registrarse():
    if request.method =='GET':
        return render_template('registro.html')
    else:
        nombre = request.form.get('nombre')
        descripcion = request.form.get('descripcion')
        imagen = request.files['imagen']
        celular = request.form.get('celular')
        direccion = request.form.get('direccion')
        correo = request.form.get('correo')
        contraseña = request.form.get('password')

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
        cuenta = cursor.fetchone()

        is_valid = True

        if cuenta:
            flash("Ya hay una empresa registrada con este correo!")
            is_valid = False

        if nombre =='':
            flash('Debe ingresar un nombre')
            is_valid = False

        if descripcion =='':
            flash('Debe ingresar una direccion')
            is_valid = False

        if imagen =='':
            flash('Debe ingresar una imagen')
            is_valid = False

        if celular =='':
            flash('Debe ingresar un numero de celular')
            is_valid = False

        if direccion =='':
            flash('Debe ingresar una direccion')
            is_valid = False

        if correo =='':
            flash('Debe ingresar un email')
            is_valid = False

        if contraseña =='':
            flash('Debe ingresar una contraseña')
            is_valid = False
            
        elif validarPassword.validarContraseña(contraseña) == False:
            flash('Contraseña no cumple con los parametros')
            is_valid= False

        if is_valid == False:
            return render_template('registro.html',nombre = nombre, descripcion = descripcion, imagen = imagen, celular = celular, direccion = direccion, correo = correo, contraseña = contraseña)
        

        #encriptar contraseña
        #encriptarPassword.encriptar(contraseña=contraseña)
        #print(contraseña)s
        contraseña = hashlib.sha1(contraseña.encode()).hexdigest()
        #insertar datos en la bd
        nombre_imagen= imagen.filename
        
        imagen.save('./stati/img/' + nombre_imagen)
        registroModels.insertarRegistro(nombre=nombre,descripcion=descripcion,imagen='/stati/img/' + nombre_imagen,celular=celular,direccion=direccion,correo=correo,contraseña=contraseña)
        
        token=s.dumps(correo, salt='email-confirm')
        link= url_for('confirmarEmail', token=token, _external=True)

        msg = EmailMessage()
        msg.set_content("Confirmar tu correo aqui: {} ".format(link))
        msg["Subject"] = "Registro de confirmacion"
        msg["From"] = settings.SMTP_EMAIL
        msg["To"] = correo
        username = settings.SMTP_EMAIL
        password = settings.SMTP_PASSWORD 
        server = SMTP("smtp.gmail.com:587")
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
        server.quit()
        flash("¡Te has registrado con éxito! REVISA TU CORREO")

        return redirect(url_for('iniciarLogin'))


@app.route("/login/confirmarEmail/<token>")
def confirmarEmail(token):
    try:
        email=s.loads(token, salt='email-confirm', max_age=60)
        cursor = db.cursor()
        cursor.execute("UPDATE usuarios SET estado='1' WHERE correo='"+email+"'")
        cursor.close()
    except SignatureExpired:
        cursor = db.cursor()
        cursor.execute("DELETE FROM usuarios WHERE correo='"+email+"' AND estado='0'")
        cursor.close()
        return "<h1>Tiempo Agotado</h1>"
    return "<h1>"+email+" ha sido confirmado tu registro correctamente</h1>"

@app.route('/login', methods=['GET','POST'])
def iniciarLogin():
    if request.method =='GET':
        return render_template("login.html")
    else:
        correo = request.form.get('correo')
        contraseña = request.form.get('contraseña')
        contraseña = hashlib.sha1(contraseña.encode()).hexdigest()

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s and contraseña=%s and estado='1'", (
            correo,
            contraseña,
            ))
        user = cursor.fetchone()

        if user:
            if contraseña == user["contraseña"]:
                session['correo'] = user['correo']
                session['contraseña'] = user['contraseña']
                return render_template('login_home.html')
            else:
                flash('contraseña/Correo incorrecta')
                return render_template("login.html")
        else:
            flash('correo/contraseña no valido')
            return render_template("login.html")
        

        '''if user:
            session["login"] = True
            session["contraseña"] = user["contraseña"]
            session["correo"] = user["correo"]
            return "¡Has iniciado sesión con éxito!"
            return render_template('login_home.html')
        else:

            flash("¡Nombre de usuario/contraseña incorrectos!")
            return render_template('login.html')
        '''

@app.route('/login/recuperarPass/<token>')
def restablecer(token):
    try:
        correo=s.loads(token, salt='nuevaPass', max_age=60)
    except SignatureExpired:
        return render_template('recuperar_Pass.html')
    return redirect(url_for('PassNew', correo=correo, _external=True))


@app.route('/login/recuperarPass', methods=['GET','POST'])
def recuPass():
    if request.method =='GET':
        return render_template('recuperar_Pass.html')
    else:
        correo = request.form.get('email_form')

        cursor =db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s and estado='1'", (
            correo,
            ))
        user = cursor.fetchone()
        cursor.close()

        if not(user):
            flash('Correo no existe')
            return render_template('recuperar_Pass.html')

        is_valid = True

        if correo =='':
            flash('Debe ingresar un email')
            is_valid = False

        if is_valid == False:
            return render_template('recuperar_Pass.html', correo = correo)

        token=s.dumps(correo, salt='nuevaPass')
        link=url_for('restablecer', token=token, _external=True)

        

        msg = EmailMessage()
        msg.set_content("Click en el enlace para restablecer contraseña: {} ".format(link))
        msg["Subject"] = "Recuperacion Password"
        msg["From"] = settings.SMTP_EMAIL
        msg["To"] = correo
        username = settings.SMTP_EMAIL
        password = settings.SMTP_PASSWORD 
        server = SMTP("smtp.gmail.com:587")
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
        server.quit()
        flash("REVISA TU CORREO")
        
        return render_template('recuperar_Pass.html')
    '''if request.method =='GET':
        return render_template('registro.html')
    else:
        correo = request.form.get('email_form')

        is_valid = True

        if correo =='':
            flash('Debe ingresar un email')
            is_valid = False

        if is_valid == False:
            return render_template('recuperar_Pass.html', correo = correo)
        

        msg = EmailMessage()
        msg.set_content("Confirmar tu correo aqui: {} ".format())
        msg["Subject"] = "Registro de confirmacion"
        msg["From"] = settings.SMTP_EMAIL
        msg["To"] = correo
        username = settings.SMTP_EMAIL
        password = settings.SMTP_PASSWORD 
        server = SMTP("smtp.gmail.com:587")
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
        server.quit()
        flash("¡Te has registrado con éxito! REVISA TU CORREO")
        
        return render_template('recuperar_Pass.html')
        '''

@app.route('/login/recuperarPass/nueva/<correo>', methods=['GET','POST'])
def PassNew(correo):
    if request.method =='GET':
        return render_template('formularioRecu.html')
    else:
        contraseña = request.form.get('contraseña')
        contraseñaR = request.form.get('contraseñaR')

        is_valid = True

        if contraseña =='':
            flash('Debe ingresar una contraseña')
            is_valid = False

        if contraseñaR =='':
            flash('Debe ingresar una contraseña')
            is_valid = False
        
        elif validarPassword.validarContraseña(contraseña) == False:
            flash('Contraseña no cumple con los parametros letra Mayuscula, caracter especial *@, un numero')
            is_valid= False
        
        elif validarPassword.validarContraseña(contraseñaR) == False:
            flash('Contraseña no cumple con los parametros letra Mayuscula, caracter especial *@, un numero')
            is_valid= False

        if is_valid == False:
            return render_template('formularioRecu.html', contraseña=contraseña, contraseñaR=contraseñaR)
         
        if contraseña==contraseñaR:

            contraseñaN=hashlib.sha1(contraseñaR.encode()).hexdigest()
            registroModels.actualizarPass(correo=correo,contraseñaN=contraseñaN)
            flash('Contraseña Actualizada')
            return render_template('login.html')
        else:
            flash('Constraseñas incorrectas')
            return render_template('formularioRecu.html')
        

app.run(debug=True)