#!/usr/bin/env python3
'''a  class to manage the API authentication'''
from flask import request
from typing import List, TypeVar


class Auth:
    '''an apin authencation class'''
    def __init__(self):
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''returns false'''
        if path is None:
            return True

        if excluded_paths is None or excluded_paths is []:
            return True

        if path[-1] != "/":
            path += "/"

        if path not in excluded_paths:
            return True
        else:
            return False

    def authorization_header(self, request=None) -> str:
        '''that returns None'''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        ''' that returns None'''
        return None
