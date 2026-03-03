from flask import render_template, request, redirect, url_for
from models import Alumnos, db
import forms
from . import alumnos


@alumnos.route("/")
@alumnos.route("/index")
def index():
    create_form = forms.UserForm(request.form)
    alumno = Alumnos.query.all()
    return render_template("alumnos/index.html",
                           form=create_form,
                           alumno=alumno)


@alumnos.route("/nuevo", methods=['GET', 'POST'])
def nuevo():
    create_form = forms.UserForm(request.form)

    if request.method == 'POST':
        alum = Alumnos(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            email=create_form.email.data,
            telefono=create_form.telefono.data
        )
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('alumnos.index'))

    return render_template("alumnos/Alumnos.html", form=create_form)


@alumnos.route("/detalles/<int:id>")
def detalles(id):
    alum = Alumnos.query.get_or_404(id)
    return render_template("alumnos/detalles.html", alumno=alum)


@alumnos.route("/modificar/<int:id>", methods=['GET', 'POST'])
def modificar(id):
    create_form = forms.UserForm(request.form)
    alum = Alumnos.query.get_or_404(id)

    if request.method == 'GET':
        create_form.id.data = alum.id
        create_form.nombre.data = alum.nombre
        create_form.apellidos.data = alum.apellidos
        create_form.telefono.data = alum.telefono
        create_form.email.data = alum.email

    if request.method == 'POST':
        alum.nombre = create_form.nombre.data
        alum.apellidos = create_form.apellidos.data
        alum.telefono = create_form.telefono.data
        alum.email = create_form.email.data
        db.session.commit()
        return redirect(url_for('alumnos.index'))

    return render_template("alumnos/modificar.html", form=create_form)


@alumnos.route("/eliminar/<int:id>", methods=['GET', 'POST'])
def eliminar(id):
    create_form = forms.UserForm(request.form)
    alum = Alumnos.query.get_or_404(id)

    if request.method == 'GET':
        create_form.id.data = alum.id
        create_form.nombre.data = alum.nombre
        create_form.apellidos.data = alum.apellidos
        create_form.telefono.data = alum.telefono
        create_form.email.data = alum.email

    if request.method == 'POST':
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('alumnos.index'))

    return render_template("alumnos/eliminar.html", form=create_form)