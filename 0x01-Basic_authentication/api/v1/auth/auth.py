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
        return False

    def authorization_header(self, request=None) -> str:
        '''that returns None'''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        ''' that returns None'''
        return None
