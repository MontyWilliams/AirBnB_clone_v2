#!/usr/bin/python3
"""module for testing airbnb clone console"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import console
import sys


class TestConsole(unittest.TestCase):
    """class for testing console of airbnb clone"""

    console = console.HBNBCommand()

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        jfile= "file.json"
        if os.path.exists(jfile):
            os.remove(jfile)

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_prompt(self):
        """test that the prompt is correct"""
        self.assertEqual(self.console.prompt, '(hbnb) ')

    def test_do_quit(self):
        with self.assertRaises(SystemExit):
            self.console.do_quit("quit")


    def test_do_create(self):
        self.console.do_create("User first_name=\"dave\"")
        with open("file.json", "r") as file:
            for line in file:
                if "first_name" in line:
                    if "dave" in line:
                        first_name = "first_name: dave"
            self.assertEqual(first_name, "first_name: dave")