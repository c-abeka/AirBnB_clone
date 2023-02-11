#!/usr/bin/python3
""" 
    The Console
"""


import cmd
from datetime import datetime


class BaseModel(cmd.Cmd):
    """ AirBnB_clone console """

    prompt = '(hbnb)'

    def do_EOF(self, arg):
        """ Exits console """
        return True
    
    def emptyline(self):
        """ Ovewrites empty line method"""
        return False

    def do_quit(self, arg):
        """ Quit command and exit the program"""
        return True

    def do_create(self, arg):
        """Create a new instance of a Model"""
        if arg:
            try:
                args = arg.split()
                
