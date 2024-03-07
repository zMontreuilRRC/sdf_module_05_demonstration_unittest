"""
Description: Module 05 demonstration: Functions with Unit Testing
Author: ACE Faculty
Date: {current date}
Usage: To execute the unit tests: 
        From the unit_testing directory in the Terminal:
        python -m unittest -v tests/test_functions.py
    To execute the python src program:
        From the unit_testing directory in the Terminal:
        python src/functions.py
"""

# Functional Testing
# Person performing manual tests and looking for problems /correct behaviour

# Unit Testing
# Tests written for the computer to run against functions
# Better code quality
# Easier debugging
# Easier refactoring
# Serve as documentation
# Continuous integration / automation

import unittest
from unittest.mock import patch

from src.functions import greet_name_age

# to run: python -m unittest -k test_greet_name_with_all_parameters
class TestGreetNameAge(unittest.TestCase):
    def test_greet_name_with_all_parameters(self):
        # Arrange: set up some variables for the test
        name = "Joe Dimaggio"
        age = 89
        expected_output = f"Hello {name}, you are {age} years old!"

        # Act: run the function or code that's being tested
        actual_output = greet_name_age(name, age)
        
        # Assert: compare some kind of expected outcome with the actual one
        self.assertEqual(expected_output, actual_output)