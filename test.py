"""Author: Sriharsha Aryasomayajula
   Date: 30-04-2023
   Position: Machine Learning Software Engineer
   3 test cases"""

import unittest
from io import StringIO
from unittest.mock import patch
from di_testcode import StringMatcher

class TestStringMatcher(unittest.TestCase):
    def setup(self):
        """Set up a StringMatcher object for each test method"""
        self.string_matcher = StringMatcher()

    def test_search_item(self):
        """Test the search_item method of StringMatcher"""
        search_term, lines = self.string_matcher.search_item()
        # Assert that the search term and lines list are as expected
        self.assertEqual(search_term, 'er')
        self.assertEqual(lines, ['"Alice was beginning...\n', 'to_get9_!very\n', '1111tired1111of1111sitting1111\n',' by her_sister.\n','on9the bank,\n','and""of""having\n','nothing to do!!!\n','er\n'])

    def test_check_file_health_valid_path(self):
        """Test the check_file_health method of StringMatcher with a valid file path"""
        error_message = self.string_matcher.check_file_health()
        # Assert that the error message is None, indicating a valid file path
        self.assertIsNone(error_message)

    def test_perform_string_operation(self):
        """Test the perform_string_operation method of StringMatcher"""
        last_line = 'er'
        lines_file = ['"Alice was beginning...\n', 'to_get9_!very\n', '1111tired1111of1111sitting1111\n',' by her_sister.\n','on9the bank,\n','and""of""having\n','nothing to do!!!\n','er\n']
        with patch('sys.stdout', new=StringIO()) as output:
            self.string_matcher.perform_string_operation(last_line, lines_file)
            # Call the perform_string_operation method with the inputs and capture the output
            self.assertEqual(output.getvalue().strip(), '[to get very]\n[by her sister]')

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)