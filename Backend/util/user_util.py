from model.user import *
import random
import string

def add_user(name, email,password):
    user = User(name=name, email=email,password=password)
    db.session.add(user)
    db.session.commit()

def get_user_by_name(name):
    return User.query.filter_by(name=name).first()

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def suggest_username(name):
    suffix_chars = string.ascii_lowercase + string.digits
    for i in range(1, 1001):
        suffix = ''.join(random.choice(suffix_chars) for _ in range(4))
        suggested_username = f'{name}_{suffix}'
        if not User.query.filter_by(name=suggested_username).first():
            return suggested_username
    return None