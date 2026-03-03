from flask import render_template, request
import forms
from models import Maestros

from . import maestros


@maestros.route("/maestros", methods=['GET','POST'])
def listado_maestros():
    create_form = forms.UserForm(request.form)
    maestros_lista = Maestros.query.all()
    return render_template("maestros/listadoMaes.html",
                           form=create_form,maestros=maestros_lista)

@maestros.route('/perfil/<nombres>')
def perfil(nombres):
    return f"Perfil de {nombres}"