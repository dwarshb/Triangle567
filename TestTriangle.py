"""
Assignment 01
@author: Darshan Bhanushali
"""

import unittest
from Triangle import Triangle	

class TestTriangle(unittest.TestCase):
	def test_invalid_triangle_input(self):
		triangle = Triangle()
		self.assertEqual(triangle.classify_triangle(0,4.2,2),'Invalid Triangle',triangle.my_brand())
		self.assertEqual(triangle.classify_triangle(0, 4, 5), 'Invalid Triangle',
			print('test_invalid_triangle_input- Passed: 0,4,5 - Only two sides have value.'))
		
	def test_equilateral(self):
		triangle = Triangle()
		self.assertEqual(triangle.classify_triangle(1, 1, 1), 'equilateral', 
			print('test_equilateral- Passed: 1,1,1 should be equilateral'))
		self.assertEqual(triangle.classify_triangle(10, 10, 10), 'equilateral')
		self.assertNotEqual(triangle.classify_triangle(0, 0, 0), 'equilateral',
			print("test_equilateral- Passed: 0,0,0 - even though 0's are equal, they can't form a triangle"))
		
	def test_isoceles(self):
		triangle = Triangle()
		self.assertNotEqual(triangle.classify_triangle(10, 10, 10), 'isoceles',
			print('test_isoceles - Passed: 10,10,10 - Should be Equilateral'))
		self.assertNotEqual(triangle.classify_triangle(10, 15, 30), 'isoceles',
			print('testPassed: 10,15,30 - Should be Scalene'))
		self.assertNotEqual(triangle.classify_triangle(10, 10, 30), 'isoceles')
		self.assertNotEqual(triangle.classify_triangle(15, 15, 30), 'isoceles')
		self.assertEqual(triangle.classify_triangle(16, 16, 30), 'isoceles')
		self.assertEqual(triangle.classify_triangle(10, 30, 30), 'isoceles',
			print('test_isoceles- Passed: 10,30,30 Right answer'))
		
	def test_right(self):
		triangle = Triangle()
		self.assertEqual(triangle.classify_triangle(3, 4, 5),'right',
			print('test_right- Passed : 3,4,5 equals right'))
		self.assertNotEqual(triangle.classify_triangle(3, 4, 6),'right',
			print('test_right - Passed : 3,4,6 not equals right'))
		
	def test_scalene(self):
		triangle = Triangle()
		self.assertEqual(triangle.classify_triangle(4, 5, 6),'scalene', 
			print('test_scalene - Passed : 4,5,6 equals scalene'))


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()