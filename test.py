import unittest
from unittest.mock import patch
from io import StringIO
import sys
from pathlib import Path
from di_testcode import StringMatcher


class TestStringMatcher(unittest.TestCase):
    def test_run(self):
        # Test case 1: Valid file path and extension
        input_file = 'test_file.txt'
        with open(input_file, 'w') as f:
            f.write('This is the first line.\n')
            f.write('This is the second line.\n')
            f.write('This is the third line.\n')
            f.write('search term\n')
        expected_output = '[This is the third line]'
        with patch('sys.stdout', new=StringIO()) as output:
            StringMatcher().run(input_file)
            self.assertEqual(output.getvalue().strip(), expected_output)

        # Test case 2: Invalid file path
        input_file = 'invalid_file.txt'
        expected_output = f'{input_file} is not a valid file path'
        with patch('sys.stderr', new=StringIO()) as error_output:
            StringMatcher().run(input_file)
            self.assertEqual(error_output.getvalue().strip(), expected_output)

        # Test case 3: Invalid file extension
        input_file = 'invalid_file.png'
        expected_output = 'Please input a text file'
        with patch('sys.stderr', new=StringIO()) as error_output:
            StringMatcher().run(input_file)
            self.assertEqual(error_output.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()