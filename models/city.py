#!/usr/bin/python3
""" Defines city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """ defines city class"""
    """ Class State  that inherits from base model """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(self, *args, **kwargs)
