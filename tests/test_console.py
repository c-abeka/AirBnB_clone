#!/usr/bin/python3
"""
    Tests The Console HBNBCommand
"""

import console
from console import HBNBCommand
import inspect
import pep8
import unittest

class TestConsoleDocs(unittest.TestCase):
    """
        Tests the documentation of the console
    """

    def test_pep8_compliance(self):
        """ Tests that the console conforms to PEP8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0, 'code failed to meet pep8 standards')

    def test_pep8_compliance_test(self):
        """ Tests that the console tests conform to PEP8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(["tests/test_console.py"])
        self.assertEqual(result.total_errors, 0, 'code failed to meet pep8 standards')

    def test_console_docstring(self):
        """ Test whether console has docstrings """
        self.assertIsNot(console.__doc__, None, "console.py does not have a docstring")

        self.assertTrue(len(console.__doc__) >= 1, "add a docstring to console.py")

    def test_HBNBCommand_class_docstring(self):
        """ Test whether Class HBNBCommand has docstrings """
        self.assertIsNot(HBNBCommand.__doc__, None, "class HBNBCommand does not have a docstring")

        self.assertTrue(len(HBNBCommand.__doc__) >= 1, "add a docstring to class HBNBCommand")
