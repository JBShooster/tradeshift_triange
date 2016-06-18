import unittest
from app_alternate import *

class MainTest(unittest.TestCase):
  def test_triangle_auto(self):
    self.assertEqual( triangle_auto(a=60,b=60,c=60), "Equilateral")
    self.assertEqual( triangle_auto(a=100,b=90,c=1), "Not a valid triangle. Largest side bigger than or equal to two smaller sides.")
    self.assertEqual( triangle_auto(a=0,b=50,c=50), "Zero or negative numbers are invalid. Try again.")
    self.assertEqual( triangle_auto(a=100,b=100,c=5), "Isosceles")
    self.assertEqual( triangle_auto(a=50,b=51,c=52), "Scalene")
    self.assertEqual( triangle_auto(a="10", b="10",c=10), "All inputs must be integers. Please try again.")

unittest.main()
