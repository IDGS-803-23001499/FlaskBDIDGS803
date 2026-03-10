from flask import render_template, request, redirect, url_for
import forms
from models import db
from models import Alumnos
from . import alumnos


@alumnos.route("/", methods=['GET'])
def alumnos_lista():
    create_form = forms.UserForm(request.form)
    alumnos = Alumnos.query.all()
    return render_template("alumnos/indexAlum.html",
                           form=create_form,
                           alumnos=alumnos)


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
        return redirect(url_for('alumnos.alumnos_lista'))

    return render_template("alumnos/nuevo.html", form=create_form)


@alumnos.route("/modificar", methods=['GET', 'POST'])
def modificar():
    create_form = forms.UserForm(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()

        create_form.id.data = id
        create_form.nombre.data = alum.nombre
        create_form.apellidos.data = alum.apellidos
        create_form.telefono.data = alum.telefono
        create_form.email.data = alum.email

    if request.method == 'POST':
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()

        alum.nombre = create_form.nombre.data
        alum.apellidos = create_form.apellidos.data
        alum.telefono = create_form.telefono.data
        alum.email = create_form.email.data

        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('alumnos.alumnos_lista'))

    return render_template("alumnos/modificar.html", form=create_form)


@alumnos.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
    create_form = forms.UserForm(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()

        create_form.id.data = id
        create_form.nombre.data = alum.nombre
        create_form.apellidos.data = alum.apellidos
        create_form.telefono.data = alum.telefono
        create_form.email.data = alum.email

    if request.method == 'POST':
        id = create_form.id.data
        alum = Alumnos.query.get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('alumnos.alumnos_lista'))

    return render_template("alumnos/eliminar.html", form=create_form)


@alumnos.route("/detalles", methods=['GET'])
def detalles():
    id = request.args.get('id')
    alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()

    return render_template("alumnos/detalles.html",
                           nombre=alum.nombre,
                           apellidos=alum.apellidos,
                           telefono=alum.telefono,
                           email=alum.email)