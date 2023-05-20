"""sample test"""
from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):
    """test the calc module"""

    def test_add_numbers(self):
        """test adding numbers"""
        
        res = calc.add(5, 6)
        self.assertEqual(res, 11)
    
    def test_substract_numbers(self):
        """substract numbers"""

        res = calc.substract(10, 15)
        self.assertEqual(res, 5)
        