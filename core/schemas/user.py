# -*- coding: utf-8 -*-
from manager import marsh


class UserSchema(marsh.Schema):
    """ Definição de schema de usuários """
    
    class Meta:
        fields = ('uuid', 'username', 'password', 'name', 'email', 'create_on')
        
 
user_schema = UserSchema()
users_schema = UserSchema(many=True)
