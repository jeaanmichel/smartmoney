# -*- coding: utf-8 -*-
from app import app
from models import Usuario, db
from forms import *
from flask import render_template, jsonify, request


@app.before_first_request
def setup():
    if not Usuario.query.filter(Usuario.username == 'jeaanmichel').first():
        user = Usuario(
            username='jeaanmichel'
        )

        db.session.add(user)
        db.session.commit()

    if not Usuario.query.filter(Usuario.username == 'usuario2').first():
        user = Usuario(
            username='usuario2' 
        )

        db.session.add(user)
        db.session.commit()

    if not Usuario.query.filter(Usuario.username == 'usuario3').first():
        user = Usuario(
            username='usuario3'
        )

        db.session.add(user)
        db.session.commit()

    if not Usuario.query.filter(Usuario.username == 'usuario4').first():
        user = Usuario(
            username='usuario4'
        )

        db.session.add(user)
        db.session.commit()


@app.route("/")
def index():

    form = MovimentacaoForm()

    usuarios = Usuario.query.all()

    return render_template("index.html", usuarios=usuarios, form=form)


@app.route("/getuserbyid", methods=["POST"])
def getblogbybid():
    id = int(request.form['id'])

    usuario = Usuario.query.filter(Usuario.id == id).one()

    json = jsonify({'id': usuario.id, 'username': usuario.username})

    return json


@app.route("/deleteuser", methods=["POST"])
def deleteuser():
    print int(request.form['id'])
    return "ola"
