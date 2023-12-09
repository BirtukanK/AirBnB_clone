#!/usr/bin/python3
""" Defines Base model unit test"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.Testcase):
    """ A class to test base model"""
    def test_no_arg(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertEqual(obj1.id, obj2.id - 1)

    def test_basemodels(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj3 = BaseModel()
        self.assertEqual(obj1.id, obj3.id - 2)

    def test_none_id(self):
        obj1 = BaseModel(None)
        obj2 = BaseModel(None)
        self.assertEqual(obj1.id, obj2.id - 1)



if __name__ == "__main__":
    unittest.main()
