# -*- coding: utf-8 -*-
from app import db


class Usuario(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(100), unique=True)