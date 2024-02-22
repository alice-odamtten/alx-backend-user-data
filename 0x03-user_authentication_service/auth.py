#!/usr/bin/env python3
'''a _hash_password method that takes in a password string arguments'''
import bcrypt


def _hash_password(password: str) -> bytes:
    '''returns bytes.'''
    return bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())
