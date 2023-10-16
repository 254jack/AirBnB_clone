#!/usr/bin/python3
"""Defines unittests for console.py.
"""
from io import StringIO
import os
import unittest
from unittest.mock import patch
from console import HBNBCommand
from models import storage
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestConsole(unittest.TestCase):
    """Base class for testing Console.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Defaults/Defaults/resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_simple(self):
        """Tests for the basic commands.
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), "\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual(f.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("?")
            self.assertIsInstance(f.getvalue(), str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIsInstance(f.getvalue(), str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? create")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), "Creates a new instance.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), "Creates a new instance.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? all")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "Prints string representation of all instances.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "Prints string representation of all instances.")

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Prints the string representation of an instance."
            HBNBCommand().onecmd("? show")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Prints the string representation of an instance."
            HBNBCommand().onecmd("help show")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Updates an instance based on the class name and id."
            HBNBCommand().onecmd("? update")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Updates an instance based on the class name and id."
            HBNBCommand().onecmd("help update")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Deletes an instance based on the class name and id."
            HBNBCommand().onecmd("? destroy")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Deletes an instance based on the class name and id."
            HBNBCommand().onecmd("help destroy")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? quit")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "Quit command to exit the program.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "Quit command to exit the program.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? help")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "To get help on a command, type help <topic>.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help help")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "To get help on a command, type help <topic>.")


class TestBaseModel(unittest.TestCase):
    """Test Basemodel commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Defaults/Defaults/resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_basemodel(self):
        """Test create_basemodel method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("BaseModel.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_basemodel(self):
        """Test all_basemodel method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all BaseModel')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[BaseModel]')

    def test_show_basemodel(self):
        """Test show_basemodel method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.eyes = "blue"
            HBNBCommand().onecmd(f'show BaseModel {b1.id}')
            res = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_basemodel(self):
        """Test update_basemodel method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.name = "Peterson"
            HBNBCommand().onecmd(f'update BaseModel {b1.id} name "Ife"')
            self.assertEqual(b1.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 85
            HBNBCommand().onecmd(f'update BaseModel {b1.id} age 25')
            self.assertIn("age", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.savings = 25.67
            HBNBCommand().onecmd(f'update BaseModel {b1.id} savings 35.89')
            self.assertIn("savings", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["savings"], 35.89)

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 60
            cmmd = f'update BaseModel {b1.id} age 10 color "blue"'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", b1.__dict__.keys())
            self.assertNotIn("color", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["age"], 10)

    def test_destroy_basemodel(self):
        """Test destroy_basemodel method.
        """
        with patch('sys.stdout', new=StringIO()):
            bm = BaseModel()
            HBNBCommand().onecmd(f'destroy BaseModel {bm.id}')
            self.assertNotIn("BaseModel.{}".format(
                bm.id), storage.all().keys())


class TestBaseModelDotNotation(unittest.TestCase):
    """Testing Basemodel commands using `.` notation.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Defaults/Defaults/resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_basemodel(self):
        """Test create_basemodel method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'BaseModel.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("BaseModel.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_basemodel(self):
        """Test count_basemodel method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('BaseModel.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == BaseModel:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_basemodel(self):
        """Test all_basemodel method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('BaseModel.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[BaseModel]')

    def test_show_basemodel(self):
        """Test show_basemodel method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.eyes = "blue"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.show({b1.id})'))
            res = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_basemodel(self):
        """Test update_basemodel method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.name = "Peterson"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.update({b1.id}, name, "Ife")'))
            self.assertEqual(b1.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 85
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.update({b1.id}, age, 25)'))
            self.assertIn("age", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 70
            cmmd = f'BaseModel.update({b1.id}, age, 10, color, blue)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", b1.__dict__.keys())
            self.assertNotIn("color", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["age"], 10)

    def test_update_basemodel_dict(self):
        """Test update_basemodel method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 85
            cmmd = f'BaseModel.update({b1.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(b1.__dict__["age"], 25)
            self.assertIsInstance(b1.__dict__["age"], int)

    def test_destroy_basemodel(self):
        """Test destroy_basemodel method.
        """
        with patch('sys.stdout', new=StringIO()):
            bm = BaseModel()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.destroy({bm.id})'))
            self.assertNotIn("BaseModel.{}".format(
                bm.id), storage.all().keys())


class TestUser(unittest.TestCase):
    """Testing the user commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Defaults/Defaults/resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_user(self):
        """Test create_user method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("User.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_user(self):
        """Test all_user method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all User')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[User]')

    def test_show_user(self):
        """Test show_user method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.eyes = "blue"
            HBNBCommand().onecmd(f'show User {us.id}')
            res = f"[{type(us).__name__}] ({us.id}) {us.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_user(self):
        """Test update_user method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.name = "Peterson"
            HBNBCommand().onecmd(f'update_user {us.id} name "Ife"')
            self.assertEqual(us.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 85
            HBNBCommand().onecmd(f'update_user {us.id} age 25')
            self.assertIn("age", us.__dict__.keys())
            self.assertEqual(us.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.savings = 25.67
            HBNBCommand().onecmd(f'update_user {us.id} savings 35.89')
            self.assertIn("savings", us.__dict__.keys())
            self.assertEqual(us.__dict__["savings"], 35.89)

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 60
            cmmd = f'update_user {us.id} age 10 color blue'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", us.__dict__.keys())
            self.assertNotIn("color", us.__dict__.keys())
            self.assertEqual(us.__dict__["age"], 10)

    def test_destroy_user(self):
        """Test destroy_user method.
        """
        with patch('sys.stdout', new=StringIO()):
            us = User()
            HBNBCommand().onecmd(f'destroy_user {us.id}')
            self.assertNotIn("User.{}".format(
                us.id), storage.all().keys())


class TestUserDotNotation(unittest.TestCase):
    """Testing the user command's dot notation.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Defaults/resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_user(self):
        """Test create_user method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'User.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("User.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_user(self):
        """Test count_user method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('User.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == User:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_user(self):
        """Test all_user method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('User.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[User]')

    def test_show_user(self):
        """Test show_user method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.eyes = "blue"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.show({us.id})'))
            res = f"[{type(us).__name__}] ({us.id}) {us.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_user(self):
        """Test update_user method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.name = "Peterson"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.update({us.id}, name, "Ife")'))
            self.assertEqual(us.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 85
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.update({us.id}, age, 25)'))
            self.assertIn("age", us.__dict__.keys())
            self.assertEqual(us.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 60
            cmmd = f'User.update({us.id}, age, 10, color, blue)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", us.__dict__.keys())
            self.assertNotIn("color", us.__dict__.keys())
            self.assertEqual(us.__dict__["age"], 10)

    def test_update_user_dict(self):
        """Test update_user method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 85
            cmmd = f'User.update({us.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(us.__dict__["age"], 25)
            self.assertIsInstance(us.__dict__["age"], int)

    def test_destroy_user(self):
        """Test destroy_user method.
        """
        with patch('sys.stdout', new=StringIO()):
            us = User()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.destroy({us.id})'))
            self.assertNotIn("User.{}".format(
                us.id), storage.all().keys())


class TestState(unittest.TestCase):
    """Testing the state commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Defaults/resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_state(self):
        """Test create_state method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create_state')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("State.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_state(self):
        """Test all_state method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all_state')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[State]')

    def test_show_state(self):
        """Test show_state method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.eyes = "blue"
            HBNBCommand().onecmd(f'show_state {st.id}')
            res = f"[{type(st).__name__}] ({st.id}) {st.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_state(self):
        """Test update_state method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.name = "Peterson"
            HBNBCommand().onecmd(f'update_state {st.id} name "Ife"')
            self.assertEqual(st.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 85
            HBNBCommand().onecmd(f'update_state {st.id} age 25')
            self.assertIn("age", st.__dict__.keys())
            self.assertEqual(st.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 60
            cmmd = f'update_state {st.id} age 10 color blue'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", st.__dict__.keys())
            self.assertNotIn("color", st.__dict__.keys())
            self.assertEqual(st.__dict__["age"], 10)

    def test_destroy_state(self):
        """Test destroy_state method.
        """
        with patch('sys.stdout', new=StringIO()):
            st = State()
            HBNBCommand().onecmd(f'destroy_state {st.id}')
            self.assertNotIn("State.{}".format(
                st.id), storage.all().keys())


class TestStateDotNotation(unittest.TestCase):
    """Testing the state command's dot notation.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Defaults/resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_state(self):
        """Test create_state method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'State.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("State.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_state(self):
        """Test count_state method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('State.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == State:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_state(self):
        """Test all_state method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('State.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[State]')

    def test_show_state(self):
        """Test show_state method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.eyes = "blue"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.show({st.id})'))
            res = f"[{type(st).__name__}] ({st.id}) {st.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_state(self):
        """Test update_state method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.name = "Peterson"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.update({st.id}, name, "Ife")'))
            self.assertEqual(st.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 85
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.update({st.id}, age, 25)'))
            self.assertIn("age", st.__dict__.keys())
            self.assertEqual(st.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 60
            cmmd = f'State.update({st.id}, age, 10, color, blue)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", st.__dict__.keys())
            self.assertNotIn("color", st.__dict__.keys())
            self.assertEqual(st.__dict__["age"], 10)

    def test_update_state_dict(self):
        """Test update_state method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 85
            cmmd = f'State.update({st.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(st.__dict__["age"], 25)
            self.assertIsInstance(st.__dict__["age"], int)

    def test_destroy_state(self):
        """Test destroy_state method.
        """
        with patch('sys.stdout', new=StringIO()):
            st = State()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.destroy({st.id})'))
            self.assertNotIn("State.{}".format(
                st.id), storage.all().keys())


class TestReview(unittest.TestCase):
    """Testing the review commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Defaults/resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_review(self):
        """Test create_review method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Review')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Review.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_review(self):
        """Test all_review method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all Review')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Review]')

    def test_show_review(self):
        """Test show review method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.eyes = "blue"
            HBNBCommand().onecmd(f'show Review {rv.id}')
            res = f"[{type(rv).__name__}] ({rv.id}) {rv.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_review(self):
        """Test update_review method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.name = "Peterson"
            HBNBCommand().onecmd(f'update Review {rv.id} name "Ife"')
            self.assertEqual(rv.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 85
            HBNBCommand().onecmd(f'update Review {rv.id} age 25')
            self.assertIn("age", rv.__dict__.keys())
            self.assertEqual(rv.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 60
            cmmd = f'update Review {rv.id} age 10 color blue)'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", rv.__dict__.keys())
            self.assertNotIn("color", rv.__dict__.keys())
            self.assertEqual(rv.__dict__["age"], 10)

    def test_destroy_review(self):
        """Test destroy_review method.
        """
        with patch('sys.stdout', new=StringIO()):
            rv = Review()
            HBNBCommand().onecmd(f'destroy Review {rv.id}')
            self.assertNotIn("Review.{}".format(
                rv.id), storage.all().keys())


class TestReviewDotNotation(unittest.TestCase):
    """Testing the review command's dot notation.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Defaults/resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_review(self):
        """Test create_review method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'Review.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Review.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_review(self):
        """Test count_review method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Review.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == Review:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_review(self):
        """Test all_review method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Review.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Review]')

    def test_show_review(self):
        """Test show review method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.eyes = "blue"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.show({rv.id})'))
            res = f"[{type(rv).__name__}] ({rv.id}) {rv.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_review(self):
        """Test update_review method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.name = "Peterson"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.update({rv.id}, name, "Ife")'))
            self.assertEqual(rv.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 85
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.update({rv.id}, age, 25)'))
            self.assertIn("age", rv.__dict__.keys())
            self.assertEqual(rv.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 60
            cmmd = f'Review.update({rv.id}, age, 10, color, blue)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", rv.__dict__.keys())
            self.assertNotIn("color", rv.__dict__.keys())
            self.assertEqual(rv.__dict__["age"], 10)

    def test_update_review_dict(self):
        """Test update_review method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 85
            cmmd = f'Review.update({rv.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(rv.__dict__["age"], 25)
            self.assertIsInstance(rv.__dict__["age"], int)

    def test_destroy_review(self):
        """Test destroy_review method.
        """
        with patch('sys.stdout', new=StringIO()):
            rv = Review()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.destroy({rv.id})'))
            self.assertNotIn("Review.{}".format(
                rv.id), storage.all().keys())


class TestPlace(unittest.TestCase):
    """Testing the place commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Defaults/resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_place(self):
        """Test create_place method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Place.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_place(self):
        """Test all_place method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all Place')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Place]')

    def test_show_place(self):
        """Test show_place method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.eyes = "blue"
            HBNBCommand().onecmd(f'show Place {pl.id}')
            res = f"[{type(pl).__name__}] ({pl.id}) {pl.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_place(self):
        """Test update_place method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.name = "Peterson"
            HBNBCommand().onecmd(f'update Place {pl.id} name "Ife"')
            self.assertEqual(pl.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.age = 85
            HBNBCommand().onecmd(f'update Place {pl.id} age 25')
            self.assertIn("age", pl.__dict__.keys())
            self.assertEqual(pl.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.age = 60
            cmmd = f'update Place {pl.id} age 10 color blue'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", pl.__dict__.keys())
            self.assertNotIn("color", pl.__dict__.keys())
            self.assertEqual(pl.__dict__["age"], 10)

    def test_destroy_place(self):
        """Test destroy_place method.
        """
        with patch('sys.stdout', new=StringIO()):
            pl = Place()
            HBNBCommand().onecmd(f'destroy Place {pl.id}')
            self.assertNotIn("Place.{}".format(
                pl.id), storage.all().keys())


class TestPlaceDotNotation(unittest.TestCase):
    """Testing the place command's dot notation.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Defaults/resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_place(self):
        """Test create_place method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'Place.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Place.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_place(self):
        """Test count_place method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Place.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == Place:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_place(self):
        """Test all_place method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Place.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Place]')

    def test_show_place(self):
        """Test show_place method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.eyes = "blue"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Place.show({pl.id})'))
            res = f"[{type(pl).__name__}] ({pl.id}) {pl.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_place(self):
        """Test update_place method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.name = "Peterson"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Place.update({pl.id}, name, "Ife")'))
            self.assertEqual(pl.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.age = 85
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Place.update({pl.id}, age, 25)'))
            self.assertIn("age", pl.__dict__.keys())
            self.assertEqual(pl.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.age = 60
            cmmd = f'Place.update({pl.id}, age, 10, color, blue)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", pl.__dict__.keys())
            self.assertNotIn("color", pl.__dict__.keys())
            self.assertEqual(pl.__dict__["age"], 10)

    def test_update_place_dict(self):
        """Test update_place method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.age = 85
            cmmd = f'Place.update({pl.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(pl.__dict__["age"], 25)
            self.assertIsInstance(pl.__dict__["age"], int)

    def test_destroy_place(self):
        """Test destroy_place method.
        """
        with patch('sys.stdout', new=StringIO()):
            pl = Place()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Place.destroy({pl.id})'))
            self.assertNotIn("Place.{}".format(
                pl.id), storage.all().keys())


class TestAmenity(unittest.TestCase):
    """Testing the amenity commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Defaults/resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_amenity(self):
        """Test create_amenity method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Amenity')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Amenity.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_amenity(self):
        """Test all_amenity method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all Amenity')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Amenity]')

    def test_show_amenity(self):
        """Test show_amenity method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.eyes = "blue"
            HBNBCommand().onecmd(f'show Amenity {am.id}')
            res = f"[{type(am).__name__}] ({am.id}) {am.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_amenity(self):
        """Test update_amenity method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.name = "Peterson"
            HBNBCommand().onecmd(f'update Amenity {am.id} name "Ife"')
            self.assertEqual(am.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.age = 85
            HBNBCommand().onecmd(f'update Amenity {am.id} age 25')
            self.assertIn("age", am.__dict__.keys())
            self.assertEqual(am.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.age = 60
            cmmd = f'update Amenity {am.id} age 10 color blue)'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", am.__dict__.keys())
            self.assertNotIn("color", am.__dict__.keys())
            self.assertEqual(am.__dict__["age"], 10)

    def test_destroy_amenity(self):
        """Test destroy_amenity method.
        """
        with patch('sys.stdout', new=StringIO()):
            am = Amenity()
            HBNBCommand().onecmd(f'destroy Amenity {am.id}')
            self.assertNotIn("Amenity.{}".format(
                am.id), storage.all().keys())


class TestAmenityDotNotation(unittest.TestCase):
    """Testing the amenity command's dot notation.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Defaults/resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_amenity(self):
        """Test create_amenity method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'Amenity.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Amenity.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_amenity(self):
        """Test count_amenity method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Amenity.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == Amenity:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_amenity(self):
        """Test all_amenity method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Amenity.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Amenity]')

    def test_show_amenity(self):
        """Test show_amenity method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.eyes = "blue"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Amenity.show({am.id})'))
            res = f"[{type(am).__name__}] ({am.id}) {am.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_amenity(self):
        """Test update_amenity method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.name = "Peterson"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Amenity.update({am.id}, name, "Ife")'))
            self.assertEqual(am.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.age = 85
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Amenity.update({am.id}, age, 25)'))
            self.assertIn("age", am.__dict__.keys())
            self.assertEqual(am.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.age = 60
            cmmd = f'Amenity.update({am.id}, age, 10, color, blue)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", am.__dict__.keys())
            self.assertNotIn("color", am.__dict__.keys())
            self.assertEqual(am.__dict__["age"], 10)

    def test_update_amenity_dict(self):
        """Test update_amenity method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.age = 85
            cmmd = f'Amenity.update({am.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(am.__dict__["age"], 25)
            self.assertIsInstance(am.__dict__["age"], int)

    def test_destroy_amenity(self):
        """Test destroy_amenity method.
        """
        with patch('sys.stdout', new=StringIO()):
            am = Amenity()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Amenity.destroy({am.id})'))
            self.assertNotIn("Amenity.{}".format(
                am.id), storage.all().keys())


class TestCity(unittest.TestCase):
    """Testing the city commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Defaults/resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_city(self):
        """Test create_city method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create City')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("City.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_city(self):
        """Test all_city method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all City')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[City]')

    def test_show_city(self):
        """Test show_city method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.eyes = "blue"
            HBNBCommand().onecmd(f'show City {cty.id}')
            res = f"[{type(cty).__name__}] ({cty.id}) {cty.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_city(self):
        """Test update_city method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.name = "Peterson"
            HBNBCommand().onecmd(f'update City {cty.id} name "Ife"')
            self.assertEqual(cty.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.age = 85
            HBNBCommand().onecmd(f'update City {cty.id} age 25')
            self.assertIn("age", cty.__dict__.keys())
            self.assertEqual(cty.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.age = 60
            cmmd = f'update City {cty.id} age 10 color blue'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", cty.__dict__.keys())
            self.assertNotIn("color", cty.__dict__.keys())
            self.assertEqual(cty.__dict__["age"], 10)

    def test_destroy_city(self):
        """Test destroy_city method.
        """
        with patch('sys.stdout', new=StringIO()):
            cty = City()
            HBNBCommand().onecmd(f'destroy City {cty.id}')
            self.assertNotIn("City.{}".format(
                cty.id), storage.all().keys())


class TestCityDotNotation(unittest.TestCase):
    """Testing the city command's dot notation.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Defaults/resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_city(self):
        """Test create_city method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'City.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("City.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_city(self):
        """Test count_city method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('City.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == City:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_city(self):
        """Test all_city method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('City.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[City]')

    def test_show_city(self):
        """Test show_city method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.eyes = "blue"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'City.show({cty.id})'))
            res = f"[{type(cty).__name__}] ({cty.id}) {cty.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_city(self):
        """Test update_city method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.name = "Peterson"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'City.update({cty.id}, name, "Ife")'))
            self.assertEqual(cty.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.age = 85
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'City.update({cty.id}, age, 25)'))
            self.assertIn("age", cty.__dict__.keys())
            self.assertEqual(cty.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.age = 60
            cmmd = f'City.update({cty.id}, age, 10, color, blue)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", cty.__dict__.keys())
            self.assertNotIn("color", cty.__dict__.keys())
            self.assertEqual(cty.__dict__["age"], 10)

    def test_update_city_dict(self):
        """Test update_city method.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.age = 85
            cmmd = f'City.update({cty.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(cty.__dict__["age"], 25)
            self.assertIsInstance(cty.__dict__["age"], int)

    def test_destroy_city(self):
        """Test destroy_city method.
        """
        with patch('sys.stdout', new=StringIO()):
            cty = City()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'City.destroy({cty.id})'))
            self.assertNotIn("City.{}".format(
                cty.id), storage.all().keys())
