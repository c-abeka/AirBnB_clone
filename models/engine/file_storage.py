#!/usr/bin/python3

'''
File Storage Module

This is in charge of class storage of the
classes
''''


import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import path

class FileStorage:
    ''' 
        Fields:
            __file_path(str): contains the path of JSON file
            with the contents of the object will be stored
            __objects(dict):stores all instance data
    '''

    __file_path = 'objects.json'
    __objects = {}

    def all(self):
        '''
            query object data
        '''

        return self.__objects
    def new(self, obj):
        ''' saves new object in __objects class attribute
            this will be serialized to the path of __file_path
            attribute in JSON.
            created_at and updated_at attr's will also be updated
        '''
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj
    
    def save(self):
        ''' 
            serializes __objects class
            
            --> "class_name.id": <class object>
        '''
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()

        with open(self.__file_path, mode='w', encodeing='utf-8') as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        ''' 
            deserializes JSON file in __file_path if it exists
            this is deserialized and appended to __objects
            like an instance
        '''

        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                json_dict = json.loads(f.read())
                for key, value in json_dict.items():
                    self.__objects[key] = eval(v['__class__'])(**values)