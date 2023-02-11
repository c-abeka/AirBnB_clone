#!/usr/bin/python3

""" city module
    
    Inherits fro BaseModel class.
    It contains the attributes to be assigned
    to the Amenities of the places.
"""
from models.base_model import BaseModel


class City(BaseModel):
    ''' city class 
        Fields:
            name(str): city 
            state_id(str): UUID of stagte or city
    '''
    state_id = ''
    name = ''

