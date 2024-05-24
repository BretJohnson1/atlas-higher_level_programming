#!/usr/bin/python3
"""
Unittesting for rectangle class
"""
import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys
from unittest.mock import patch, MagicMock
import json


class TestRectangle(unittest.TestCase):
    """
    class for testing Rectangle class
    """
    def test_valid_attributes_2(self):
        ''' test valid attribute value * 2'''
        rectangle = Rectangle(10, 99)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 99)

    def test_valid_attributes_4(self):
        ''' test valid attribute values * 4'''
        rectangle = Rectangle(10, 20, 5, 5)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        slef.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 5)

    def test_valid_attributes_5(self):
        ''' test valid attribute values * 5'''
        rectangle = Rectangle(10, 20, 5, 5, 99)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 5)
        self.assertEqual(rectangle.id, 99)

    def test_invalid_width(self):
        ''' test invalid width values'''
        with self.assertRaises(TypeError):
            Rectangle("string", 20, 5, 5)

    def test_invalid_height(self):
        ''' test invalid height values'''
        with self.assertRaises(TypeError):
            Rectangle(20, "string", 5, 5)

    def test_invalid_x(self):
        ''' test invalid x values'''
        with self.assertRaises(TypeError):
            Rectangle(5, 20, "string", 5)

    def test_invalid_y(self):
        ''' test invalid y values'''
        with self.assertRaises(TypeError):
            Rectangle(5, 20, 99, "string")

    def test_negative_width(self):
        ''' test negative width'''
        with self.assertRaises(ValueError):
            Rectangle(-2, 3)

    def test_negative_height(self):
        ''' test negative height'''
        with self.assertRaises(ValueError):
            Rectangle(2, -3)

    def test_zero_width(self):
        ''' test zero width'''
        with self.asseertRaises(ValueError):
            Rectangle(0, 3)

    def test_zero_height(self):
        ''' test zero height'''
        with self.assertRaises(ValueError):
            Rectangle(5, 0)

    def test_negative_x(self):
        ''' test negative x'''
        with self.assertRaises(ValueError):
            Rectangle(1, 5, -2, 3)

    def test_negative_y(self):
        ''' test negative y'''
        with self.assertRaises(ValueError):
            Rectangle(1, 5, 2, -6)

    def test_area(self):
        r1 = Rectangle(5, 10)
        result = r1.area()
        self.assertEqual(result, 50)

    def test_str(self):
        r1 = Rectangle(5, 10, 2, 3, 1)
        slef.assertEqual(str(r1), "[Rectangle] (1) 2/3 - 5/10")

    def test_display_without_xy(self):
        r1 = Rectangle(5, 3)

        # Redirect stdout to capture the output
        captured_output = StringIO()
        sys.stdout = captured_output

        r1.display()

        # Restore the original stdout
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), "#####\n#####\n#####\n")

    def test_display(self):
        r1 = Rectangle(5, 3, 2, 2, 1)

        # Redirect stdout to capture the output
        captured_output = StringIO()
        sys.stdout = captured_output

        r1.display()

        # Restore the original stdout
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), "\n\n #####\n #####\n #####\n")

    def test_to_dict(self):
        r1 = Rectangle(2, 3, 1, 1, 99)

        self.assertEqual(r1.to_dictionary(), {'id': 99, 'width': 2, 'height': 3, 'x': 1, 'y': 1})

    def test_update(self):
        r1 = Rectangle(5, 3, 2, 2, 1)
        r1.update(10, 7, 4, 4, 3)

        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 7)
        self. assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 3)

    def test_create(self):
        r1 = Rectangle.create(**{'id': 89})

        self.assertEqual(r1.id, 89)

    def test_save_to_file_with_none(self):
        # Path the open function to capture the file output
        with patch('builtins.open', create=True) as mock_open:
            # Call the save_to_file method with None
            Rectangle.save_to_file(None)

            # Assert that open was called with the correct filename
            mock_open.assert_called_once_with('Rectangle.json', 'w')

            # Retrieve the write call arguments
            write_args = mock_open.return_value.__enter__.return_value.write.call_args[0]

            # Convert the json string to a dictionary
            saved_data = json.loads(write_args[0])

            # Assert that the saved data is an empty list
            self.assertEqual(saved_data, [])

    def test_save_to_file_with_empty_brackets(self):
        # Patch the open fucntion to capture the file output
        with patch('builtins.open', create=True) as mock_open:
            # Call the save_to_file method with None
            Rectangle.save_to_file([])

            # Assert that open was called with the correct filename
            mock_open.assert_called_once_with('Rectangle.json', 'w')

            # Retrieve the write call arguments
            write_args = mock_open.return_value.__enter__.return_value.write.call_args[0]

            # Convert the json string to a dictionary
            saved_data = json.loads(write_args[0])

            # Assert that the saved data is an empty list
            self.assertEqual(saved_data, [])

    def test_save_to_file_with_single_rectangle(self):
        # Create a rectangle instance
        r1 = Rectangle(1, 2)

        # Patch the open function to capture the file output
        with patch('builtins.open', create=True) as mock_open:
            # Call the save_to_file method with a list containing the rectangle
            Rectangle.save_to_file([r1])

            # Assert that open was called with the correct filename
            mock_open.assert_called_once_with('Retcangle.json', 'w')

            # Retrieve the write call arguments
            write_args = mock_open.return_value.__enter__.return_value.write.call_args[0]

            # Convert the json string to a dictionary
            saved_data = json.loads(write_args[0])

            # Assert that the saved data is a list with  a single rectangle dictionary
            self.assertEqual(len(saved_data), 1)
            self.assertEqual(saved_data[0]['id'], r1.id)
            self.assertEqual(saved_data[0]['width'], r1.width)
            self.assertEqual(saved_data[0]['height'], r1.height)
            self.assertEqual(saved_data[0]['x'], r1.x)
            self.assertEqual(saved_data[0]['y'], r1.y)

    @patch('builtins.open', new_callable=MagicMock)
    def test_load_from_file_not_found(self, mock_open):
        mock_open.side_effect = FileNotFoundError
        mock_open.return_value.__enter__.return_value.read.return_value = ""

        # Call the load_from_file method
        result = Rectangle.load_from_file()

        # Assert that open was called with the correct filename
        mock_open.assert_called_once_with('Retcangle.json', 'r', encoding='utf-8')

        # Assert that the result is an empty list
        slef.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()