import unittest
from app import *

class MainTest(unittest.TestCase):
  def test_triangle_type(self):
    self.assertEqual( triangle_type(a=60,b=60,c=60), "Equilateral")
    self.assertEqual( triangle_type(a=0,b=50,c=50), "Not a triangle")

unittest.main()
