from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class PostForm(Form):
    publicacion = StringField('Comentario', validators=[DataRequired()])
