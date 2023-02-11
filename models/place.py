#!/usr/bin/python3

""" place module
    
    Inherits fro BaseModel class.
    It contains the attributes to be assigned
    to the Amenities of the places.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    ''' Place class 
        Fields:
            city_id(str): uuid of city
            user_id(str): uuid of user
            name(str): place name
            description(str): place description
            number_rooms(int): total rooms in place
            number_bathrooms(int): total bathrooms
            max_guest(int): max guests accomodable
            price_by_night(int): price per night
            latitude(float): latitude of place
            longitude(float): longitude of place
            amenity_ids(list): all amenities in place
    '''
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

