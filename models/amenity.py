#!/usr/bin/python3

""" Amenity module
    
    Inherits fro BaseModel class.
    It contains the attributes to be assigned
    to the Amenities of the places.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    ''' Amenity class 
        Fields:
            name(str): amenity name
    '''
    name = ''

