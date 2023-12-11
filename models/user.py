#!/usr/bin/python3
""" Defines user class"""
from models.base_model import BaseModel

class User(BaseModel):
    """ User class that inherits from BaseModel""" 
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""
