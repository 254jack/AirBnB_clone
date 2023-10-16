#!/usr/bin/python3
"""Tests for the city module.
"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.city import City
from datetime import datetime

c1 = City()
c2 = City(**c1.to_dict())
c3 = City("hi", "wait", "at")


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Defaults/resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test case for the class attributes"""
        k = f"{type(c1).__name__}.{c1.id}"
        self.assertIsInstance(c1.name, str)
        self.assertEqual(c3.name, "")
        c1.name = "Abuja"
        self.assertEqual(c1.name, "Abuja")

    def test_init(self):
        """Test case for the public instances"""
        self.assertIsInstance(c1.id, str)
        self.assertIsInstance(c1.created_at, datetime)
        self.assertIsInstance(c1.updated_at, datetime)
        self.assertEqual(c1.updated_at, c2.updated_at)

    def test_save(self):
        """Test case for save"""
        old_update = c1.updated_at
        c1.save()
        self.assertNotEqual(c1.updated_at, old_update)

    def test_todict(self):
        """Test case for dict"""
        a_dict = c2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(c2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(c1, c2)


if __name__ == "__main__":
    unittest.main()
