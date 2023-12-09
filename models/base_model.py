#!/usr/bin/python3
""" Defines BaseModel class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """ Base model class that defines all common attributes/methods
    for other classes"""

    def __init__(self, *args, **kwargs):
        """ init method for the base class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """ Save method to update public istance attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary"""
        instance_dict = self.__dict__.copy()
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        instance_dict["__class__"] = self.__class__.__name__

        for key, value in self.__dict__.items():
            if ((key not in {'created_at', 'updated_at'}) and
               (key not in instance_dict)):
                instance_dict[key] = value
        return instance_dict

    def __str__(self):
        """defines classe"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))
