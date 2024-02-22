#!/usr/bin/env python3
'''a _hash_password method that takes in a password string arguments'''
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    '''returns bytes.'''
    return bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        ''' mandatory email and password'''
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            user = self._db.add_user(email, _hash_password(password))
            return user