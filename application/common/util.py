# encoding=utf8

import uuid
import hashlib
import time

import bcrypt


def generate_password(password, rounds=10):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(rounds))


def is_correct_password(password, hashed):
    return bcrypt.hashpw(password.encode("utf-8"), hashed.encode("utf-8")) == hashed


def generate_inv_code():
    salt = str(uuid.uuid4())
    salt = salt.split('-')[0]
    m = hashlib.md5()
    m.update(salt + str(time.time()))
    return m.hexdigest()[:8]
