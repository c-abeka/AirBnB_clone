#!/usr/bin/python3

"""
    The BaseModel Module
    ____________________

    This module extablishes a reference
    for the rest of the classes of the project.
    From this it is possible to extract information
    like unique id, datetime of class creation
    and update, standard format to print class
    content, how to save data created from the 
    instances and the representation of all 
    the keys and values of an instance.
"""

from datetime import datetime
import uuid
import models

class BaseModel:
    """
        This class takes care of initialization,
        serialization and deserialization of 
        future instances.
        
        Fields
        ------
        id(str): This is a unique id(UUID) for when
        an instance is created.
        created_at(datetime): The current date of 
        instance creation.
        updated_at: The date and time when a created instance
        was updated.
    """
    format_data = '%Y-%m-%d %H:%M:%S.%f'
    

    def __init__(self, *args, **kwargs):
        """ BaseModel initialization """

        if kwargs:
            for key, value in kwargs.items():
                if arg in ('created_at', 'updated_at'):
                    value = datetime.strptime(value, format_data)

                if arg != '__class__':
                    setattr(self, arg, val)
        else;
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        ''' string representation of class '''

        return '[{0}] ({1}) ({2})'.format(self.__class__.name, self.id, self.__dict__)

    def save(self):
        ''' updates base  model 
        
            updates public instance updated_at
            with the current datetime
        '''

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' converts class info and makes it readable '''

        class_data = self.__dict__.copy()
        class_data['__class__'] = self.__class__.__name__
        class_data['created_at'] = self.created_at.isoformat()

