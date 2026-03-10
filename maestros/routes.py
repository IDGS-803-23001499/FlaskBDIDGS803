from flask import render_template, request, redirect, url_for
import forms
from models import db
from models import Maestros
from . import maestros

@maestros.route("/", methods=['GET'])
def listado_maestros():
    create_form = forms.MaesForm(request.form)
    maestros = Maestros.query.all()
    return render_template("maestros/listadoMaes.html",
                           form=create_form,maestros=maestros)

@maestros.route('/perfil/<nombres>')
def perfil(nombres):
    return f"Perfil de {nombres}"

@maestros.route("/nuevo", methods=['GET', 'POST'])
def nuevo():
    create_form = forms.MaesForm(request.form)

    if request.method == 'POST':
        maes = Maestros(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            especialidad=create_form.especialidad.data,
            email=create_form.email.data
        )
        db.session.add(maes)
        db.session.commit()
        return redirect(url_for('maestros.listado_maestros'))

    return render_template("maestros/nuevo.html", form=create_form)


@maestros.route("/modificar", methods=['GET', 'POST'])
def modificar():
    create_form = forms.MaesForm(request.form)

    if request.method == 'GET':
        matricula = request.args.get('matricula')
        maes = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()

        create_form.matricula.data = matricula
        create_form.nombre.data = maes.nombre
        create_form.apellidos.data = maes.apellidos
        create_form.especialidad.data = maes.especialidad
        create_form.email.data = maes.email

    if request.method == 'POST':
        matricula = create_form.matricula.data
        maes = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()

        maes.nombre = create_form.nombre.data
        maes.apellidos = create_form.apellidos.data
        maes.especialidad = create_form.especialidad.data
        maes.email = create_form.email.data

        db.session.commit()
        return redirect(url_for('maestros.listado_maestros'))

    return render_template("maestros/modificar.html", form=create_form)


@maestros.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
    create_form = forms.MaesForm(request.form)

    if request.method == 'GET':
        matricula = request.args.get('matricula')
        maes = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()

        create_form.matricula.data = matricula
        create_form.nombre.data = maes.nombre
        create_form.apellidos.data = maes.apellidos
        create_form.especialidad.data = maes.especialidad
        create_form.email.data = maes.email

    if request.method == 'POST':
        matricula = create_form.matricula.data
        maes = Maestros.query.get(matricula)
        db.session.delete(maes)
        db.session.commit()
        return redirect(url_for('maestros.listado_maestros'))

    return render_template("maestros/eliminar.html", form=create_form)


@maestros.route("/detalles", methods=['GET'])
def detalles():
    matricula = request.args.get('matricula')
    maes = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()

    return render_template("maestros/detalles.html",
                           nombre=maes.nombre,
                           apellidos=maes.apellidos,
                           especialidad=maes.especialidad,
                           email=maes.email)