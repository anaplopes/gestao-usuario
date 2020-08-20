# -*- coding: utf-8 -*-
from manager import db
from manager import marsh
from datetime import datetime
from core.utils.generate_uuid import generate_uuid


class UserModel(db.Model):
    """ Definição de tabela de usuários """
    
    __tablename__ = 'user'
    
    uuid = db.Column(db.String(), primary_key=True, default=generate_uuid())
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    create_on = db.Column(db.DateTime, default=datetime.now())
    isActive = db.Column(db.Boolean, default=True)
    
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email


db.create_all()
db.session.commit()


class UserSchema(marsh.Schema):
    """ Definição de schema de usuários """
    
    class Meta:
        fields = ('uuid', 'username', 'password', 'name', 'email', 'create_on', 'isActive')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
