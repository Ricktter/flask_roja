from app import app
from flask import render_template
from forms.forms import PostForm
from facebook_api.usuario import Usuario


@app.route("/")
def index():
    contexto = ["Elisa", "Alejandro", "David"]
    return render_template("index.html", data=contexto)


@app.route("/saludo")
def hello():
    return "hola mundo"


@app.route("/usuario/<user>")
def perfil(user):
    return "hola mundo %s" % user


@app.route("/face_name")
def getName():
    user = Usuario()
    respuesta = user.obtenInformacion()
    return render_template("usuario.html", data=respuesta)


@app.route("/api", methods=('GET', 'POST'))
def api():
    miForm = PostForm()
    if miForm.validate_on_submit():
        user = Usuario()
        respuesta = user.publicarComentario(miForm.publicacion.data)
        if respuesta is not False:
            return render_template("comentario.html", data=respuesta["id"], form=miForm)
        else:
            return render_template("404.html")
    else:
        return render_template("comentario.html", data=Usuario().id_coment, form=miForm)
