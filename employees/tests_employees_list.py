#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
import tempfile
import unittest
import json
from StringIO import StringIO
from flask import Flask, Blueprint
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from employees.frontend import frontend
from employees.factory import create_app
from flask_testing import TestCase


class employeeListTest(TestCase):

    def create_app(self):
        app = create_app('test_config.py')
        
        return app

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_homepage(self):
        with self.app.test_client() as client:
            rv = client.get('/',  follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'Challenge', rv.data)

    def test_obtain_employees(self):
        """ List of employees that are Male which birth date is 1965-02-01 and the hire date """
        """ is greater than 1990-01-01 ordered by the Full Name of the employee. """
        with self.app.test_client() as client:
            rv = client.get('/show',  follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'Felipe Zipitria', rv.data)

if __name__ == '__main__':
    unittest.main()
