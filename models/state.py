#!/usr/bin/python3
''' State Module 
    contains state attributes
'''

from models.base_model import BaseModel


class State(BaseModel):
    ''' State Class

        Fields:
            name(str): state name
    '''

    name = ''