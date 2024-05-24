#!/usr/bin/python3
"""
Unittest module for Base class
"""
import unittest
from models.base import Base
from unittest.mock import patch
from io import StringIO


class TestBase(unittest.TestCase):
    """
    class for testing Base class
    """
    def test_auto_id_assign(self):
        """ Auto assign ID exists"""
        b1 = Base()
        b2 = Base()
        b3 = Base(99)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 99)

    def test_id_type(self):
        """ test the type to ensure an integer"""
        base = Base(99)
        self.assertisinstance(base.id, int)

    def test_to_json_empty(self):
        """ test empty to json"""
        with self.assertRaises(TypeError):
            b1 = Base()
            json_dictionary = Base.to_json_string()

    @patch('sys.stdout', new_callable=StringIO)
    def test_to_json_string_with_none(self, mock_stdout):
        expected_output = "[]"
        result = Base.to_json_string(None)
        self.assertEqual(result, expected_output)
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_from_json_string_with_none(self, mock_stdout):
        expected_output = []
        result = Base.from_json_string(None)
        self.assertEqual(result, expected_output)
        self.assertEqual(mock_stdout.getvalue(), "")

if __name__ == '__main__':
    unittest.main()