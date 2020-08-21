# -*- coding: utf-8 -*-
import hashlib


def generate_avatar(email):
    """ Responsável pela criação do avatar """
    
    prefix = 'https://www.gravatar.com/avatar/'
    suffix = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
    arg = '?r=pg&d=identicon'
    
    gravatar =  prefix + suffix + arg
    return gravatar
