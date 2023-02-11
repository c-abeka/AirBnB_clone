#!/usr/bin/python3
'''
User Module

contains user information
'''

from models.base_model import BaseModel


class User(BaseModel):
    '''
        User Class

        Fields:
            email(str): User email
            password(str): user password
            first_name(str): user first name
            last_name(str): user last name
    '''

    email = ''
    password = ''
    first_name = ''
    last_name = ''