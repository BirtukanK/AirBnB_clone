#!/usr/bin/python3
"""defines unit test for filestorage class"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ unittest class """
    def setUp(self):
        """creates instance of Filestorage for testing"""
        self.file_storage = FileStorage()

    def test_all(self):
        """ Tests all method"""
        result = self.file_storage.all()
        self.assertIsInstance(result, dict)

    def test_new(self):
        """ Tests if new method adds an object to the dictionary"""
        user = User()
        self.file_storage.new(user)
        result = self.file_storage.all()
        self.assertIn("User.{}".format(user.id), result)

    def test_save_and_reload(self):
        """ Tests save and reload methods"""
        user = User()
        self.file_storage.new(user)
        self.file_storage.save()

        new_file_storage = FileStorage()
        new_file_storage.reload()

        result = new_file_storage.all()
        self.assertIn("User.{}".format(user.id), result)


if __name__ == "__main__":
    unittest.main()
