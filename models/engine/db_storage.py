#!/usr/bin/python3
"""This module defines a class to manage file storage for using a database
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session, scoped_session
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv


class DBStorage:
    """This class manages storage of hbnb models in SQL format
    """

    __engine = None
    __session = None

    def __init__(self):
        """Instantiates Instance into DBStorage using env vars
        """
        dialect = "mysql"
        driver = "mysqldb"
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('{}+{}://{}:{}@{}/{}'
                                      .format(dialect, driver,
                                              user, passwd, host,
                                              db), pool_pre_ping=True)
        env = os.getenv("HBNB_ENV")
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Retrieves all objects from session"""
        classes = (City, State, User, Place, Amenity, Review)

        all_dict = {}
        if cls is None:
            for i in classes:
                for obj in self.__session.query(i):
                    all_dict["{}.{}".format(i.__name__, obj.id)] = obj
        elif cls in classes:
            for obj in self.__session.query(cls):
                all_dict["{}.{}".format(cls.__name__, obj.id)] = obj
        return all_dict

    def new(self, obj):
        """ add an object to the session
        """
        self.__session.add(obj)

    def save(self):
        """ save an object to the session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete an object from the session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Retrieves all objects on start-up"""
        Base.metadata.create_all(self.__engine)
        session_rel = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_rel)
        self.__session = Session

    def close(self):
        """calls remove method on private session attribute"""
        self.__session.remove()
