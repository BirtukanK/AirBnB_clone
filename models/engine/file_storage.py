#!/usr/bin/python3
""" Defines FileStorage class"""
import json
from models.base_model import BaseModel

class FileStorage:
    """ File storage class that serializes and deserializes instances to and from JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Method to return dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects"""
        key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key, obj.id)] = obj
        
    def save(self):
        """ serializes the dictionary to the JSON file"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(objdict, json_file)

    def reload(self):
        """ Deserializes the JSON file"""
        try:
            with open(FileStorage.__file_path, "r") as json_file:
                objdict = json.load(json_file)
        except:
            pass