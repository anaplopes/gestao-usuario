# -*- coding: utf-8 -*-
from manager import db
from datetime import datetime
from utils.generate_uuid import generate_uuid


class User(db.Model):
    """ Definição de tabela de usuários """
    
    uuid = db.Column(db.String(), primary_key=True, default=generate_uuid())
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(8), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    create_on = db.Column(db.DateTime, default=datetime.now())
    isActive = db.Column(db.Boolean, default=True)
    
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
