#!/usr/bin/python3
""" Defines State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """ A State class which defines staet of user"""
    self.name = ""
    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(self, *args, **kwargs)
