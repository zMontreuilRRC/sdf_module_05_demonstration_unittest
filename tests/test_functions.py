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
# Mocks, Stubs, Fakes, etc.

from src.functions import greet_name_age
from src.functions import grade_outcome
from src.functions import prompt_name_greeting
from src.functions import math_operation

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

class TestGradeOutcome(unittest.TestCase):

    def test_grade_outcome_a_plus(self):
        #Arrange
        test_grade = 91
        expected = "A+"

        #Act
        actual = grade_outcome(test_grade)

        #Assert
        self.assertEqual(expected, actual)
        # Act and Assert
        # self.assertEqual(grade_outcome(test_grade), actual)

    def test_grade_outcome_pass(self):
        #Arrange
        test_grade = 76
        low_edge = 50
        high_edge = 90
        expected = "Pass"

        #Assert and Act
        self.assertEqual(expected, grade_outcome(test_grade))
        self.assertEqual(expected, grade_outcome(low_edge))
        self.assertEqual(expected, grade_outcome(high_edge))

    def test_grade_outcome_fail(self):
        #Arrange
        test_grade = 40
        negative = -1
        expected = "Fail"

        #Act
        actual = grade_outcome(test_grade)

        #Assert
        self.assertEqual(expected, actual)
        self.assertEqual(expected, grade_outcome(negative))
        # Act and Assert
        # self.assertEqual(grade_outcome(test_grade), actual)

class TestPromptNameGreeting(unittest.TestCase):
    def test_prompt_name_greeting_correct_output(self):
        with patch("builtins.input") as mock_input:
            # Arrange
            name = "Joe"
            city = "Winnipeg"

            mock_input.side_effect = [name, city]

            expected = f"Your name is {name} and your current city is {city}."

            # Act
            actual = prompt_name_greeting()

            # Assert
            self.assertEqual(expected, actual)

class TestMathOperation(unittest.TestCase):
    def test_math_operation_bad_operator_raises_exception(self):
        # arrange
        operand_one = 20
        operand_two = 30
        operator = "*"
        expected = "Invalid operation."

        # Act and Assert
        with self.assertRaises(ValueError) as context:
            math_operation(operand_one, operand_two, operator)

        self.assertEqual(expected, str(context.exception))

    def test_math_operation_bad_operator_raises_exception(self):
        # arrange
        operand_one = "2O"
        operand_two = 30
        operator = "+"

        # Act and Assert
        with self.assertRaises(TypeError) as context:
            math_operation(operand_one, operand_two, operator)