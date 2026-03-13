from flask import render_template, request, redirect, url_for
from models import db, Curso, Maestros, Alumnos
from . import cursos


@cursos.route("/")
def listado_cursos():
    cursos = Curso.query.all()
    return render_template("cursos/listadoCursos.html", cursos=cursos)


@cursos.route("/nuevo", methods=['GET','POST'])
def nuevo():

    maestros = Maestros.query.all()

    if request.method == 'POST':

        curso = Curso(
            nombre=request.form['nombre'],
            descripcion=request.form['descripcion'],
            maestro_id=request.form['maestro']
        )

        db.session.add(curso)
        db.session.commit()

        return redirect(url_for('cursos.listado_cursos'))

    return render_template("cursos/nuevo.html", maestros=maestros)


@cursos.route("/inscribir", methods=['GET','POST'])
def inscribir():

    alumnos = Alumnos.query.all()
    cursos = Curso.query.all()

    if request.method == 'POST':

        alumno = Alumnos.query.get(request.form['alumno'])
        curso = Curso.query.get(request.form['curso'])

        curso.alumnos.append(alumno)

        db.session.commit()

        return redirect(url_for('cursos.listado_cursos'))

    return render_template(
        "cursos/inscribir.html",
        alumnos=alumnos,
        cursos=cursos
    )

@cursos.route("/consultas", methods=['GET','POST'])
def consultas():

    alumnos = Alumnos.query.all()
    cursos = Curso.query.all()

    return render_template(
        "cursos/consultas.html",
        alumnos=alumnos,
        cursos=cursos
    )


@cursos.route("/alumnos/<int:curso_id>")
def alumnos_curso(curso_id):

    curso = Curso.query.get_or_404(curso_id)

    return render_template(
        "cursos/alumnos_curso.html",
        curso=curso,
        alumnos=curso.alumnos
    )


@cursos.route("/cursos/<int:alumno_id>")
def cursos_alumno(alumno_id):

    alumno = Alumnos.query.get_or_404(alumno_id)

    return render_template(
        "cursos/cursos_alumno.html",
        alumno=alumno,
        cursos=alumno.cursos
    )