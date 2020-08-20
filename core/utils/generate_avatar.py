# -*- coding: utf-8 -*-
import hashlib


def generate_avatar(email):
    """Create avatar."""
    
    prefix = 'https://www.gravatar.com/avatar/'
    suffix = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
    arg = '?r=pg&d=identicon'
    
    gravatar =  prefix + suffix + arg
    return gravatar
