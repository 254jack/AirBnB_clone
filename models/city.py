#!/usr/bin/python3
"""`city` module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class inheriting from BaseModel
    """
    name = ""
    state_id = ""
