#!/usr/bin/python3
"""This module defines a class to manage file storage for using a database
"""
import os
from models.base_model import Base, BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session, scoped_session


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
        """ import modules
        """
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = (City, State, User, Place, Amenity, Review)
        
        my_dict = {}
        for i in classes:
            if cls is None or cls == i:
                our_objs = self.__session.query(classes[i]).all()
                for obj in our_objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    my_dict.update({key: obj})
        return (my_dict)

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
        """ This method sets the engine and loads the session
        """


        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()


    def close(self):
        """ remove
        """
        self.__session.remove()
