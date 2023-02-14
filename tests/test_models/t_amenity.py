#!/usr/bin/python3
''' Test Amenity '''

from datetime import datetime
import models
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8
import unittest
import os

class TestAmenity(unittest.TestCase):
    ''' This tests the Amenity Class '''


    @classmethod
    def setUpClass(cls):
        ''' set the class for a test '''
        cls.amenity = Amenity()
        cls.amenity.name = "SummerHouse"

    @classmethod
    def tearDown(cls):
        ''' teardown method '''

        del cls.amenity
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_pep8_conformance_amenity(self):
        ''' test that pep8 standards are maintained '''
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, 'Found pep8 errors (and warnings).')

    def test_check_docstring_amenity(self):
        ''' check whether docstring exists '''
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_amenity(self):
        ''' check whether amenity has attributes '''
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_save_amenity(self):
        ''' test if save method works '''
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict_amenity(self):
        ''' test if to_dict works '''
        self.assertEqual('to_dict' in dir(self.amenity), True)

    def test_class(self):
        ''' test if class is named correctly '''
        self.assertEqual(self.amenity.__class__.name, 'Amenity')

    def test_parent(self):
        ''' test wheter it inherits from BaseModel '''
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel))

if __name__ == "__main__":
    unittest.main()

