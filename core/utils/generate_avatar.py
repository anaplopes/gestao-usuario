# -*- coding: utf-8 -*-
import hashlib


def generate_avatar(email):
    """Create avatar."""
    
    gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower().encode('utf-8')).hexdigest() + "?f=y&r=pg&d=mp"
    return gravatar_url
