#!/usr/bin/python3
""" Defines user class"""
import BaseModel

class User(BaseModel):
    """ User class that inherits from BaseModel"""
    def __init__(self):
        """ Initializes Usser class"""
        super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
