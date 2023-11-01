#!/usr/bin/python3
""" holds class Client"""
import hashlib
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Client(BaseModel, Base):
    """Representation of a client """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        phone = Column(Integer(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        garbage_type = relationship(
            "Garbage_type",
            cascade="all, delete, delete-orphan",
            backref="client"
        )
        garbage_collection_company = relationship(
            "Garbage_collection_company",
            cascade="all, delete, delete-orphan",
            backref="client"
        )
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        phone = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, __name: str, __value) -> None:
        '''Sets an attribute of this class to a given value.'''
        if __name == 'password':
            if type(__value) is str:
                m = hashlib.md5(bytes(__value, 'utf-8'))
                super().__setattr__(__name, m.hexdigest())
        else:
            super().__setattr__(__name, __value)
