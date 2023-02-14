#!/usr/bin/python3
""" 
    The Console
    
    The console controls all databases can
    create, modify or delete instances.
"""

import cmd
from datetime import datetime
import models
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel
import shlex

classes = {
        "BaseModel":BaseModel, 
        "Amenity": Amenity, 
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User
        }


class HBNBCommand(cmd.Cmd):
    """ AirBnB_clone console """

    prompt = '(hbnb)'

    def do_EOF(self, arg):
        """ Exits console """
        return True
    
    def emptyline(self):
        """ Ovewrites empty line method"""
        return False

    def do_quit(self, arg):
        """ Quit command exits the program"""
        return True
    
    def _key_value_parser(self, args):
        """ Creates a dict object form a list of strings """
        new_dict = {}
        for arg in args:
            if "=" in args:
                key_value = arg.split("=", 1)
                key = key_value[0]
                value = key_value[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """ Creates a new instance of a model """
        
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dict = self.key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """ 
            Prints a string format of a class instance 
            based on class and id 
        """

        args = shlex.split(arg)
        if len(args) == 0:
            print('** class name missing **')
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """ Delete an instance of a class based on the class and id """
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
