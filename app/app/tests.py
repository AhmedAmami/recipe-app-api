"""
Simple tests
"""
from django.test import TestCase
from app import calc
class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        res = calc.add(3, 8)
        self.assertEqual(res, 11)
    def test_substract_numbers(self):
        """Test that values are subtracted and returned"""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
