# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertNotEqual(classifyTriangle(3, 4, 6),'Right','3,4,6 not equals right')

    def testEquilateralTriangleA(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangleB(self):
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral','10,10,10 is equilateral')

    def testEquilateralTriangleC(self):
        self.assertNotEqual(classifyTriangle(0, 0, 0), 'Equilateral','even though 0 are equal, they cant form a triangle')

    def testInvalidTriangleA(self):
    	self.assertEqual(classifyTriangle(0,4.2,2),'InvalidInput','0,4.2,2 are Invalid input')

    def testInvalidTriangleB(self):
    	self.assertEqual(classifyTriangle(3.5,1.2,2.2),'InvalidInput','3.5,1.2,2.2 are Invalid input')

    def testInvalidTriangleC(self):
    	self.assertEqual(classifyTriangle(0, 4, 5), 'NotATriangle','0,4,5 - Only two sides have value.')

    def testIsocelesTriangleA(self):
        self.assertNotEqual(classifyTriangle(10, 10, 10), 'Isoceles','10,10,10 - Should be Equilateral')

    def testIsocelesTriangleB(self):
        self.assertNotEqual(classifyTriangle(10, 15, 30), 'Isoceles','10,15,30 - Should be Scalene')

    def testIsocelesTriangleC(self):
        self.assertNotEqual(classifyTriangle(10, 10, 30), 'Isoceles', '10,10,30 can be isoceles, but 10+10=20 < 30')

    def testIsocelesTriangleD(self):
        self.assertNotEqual(classifyTriangle(15, 15, 30), 'Isoceles','15,15,30 can be isoceles, but 15+15=30 == 30')

    def testIsocelesTriangleE(self):
        self.assertEqual(classifyTriangle(16, 16, 30), 'Isoceles','16+16=32 > 30 and it is isoceles')

    def testIsocelesTriangleF(self):
        self.assertEqual(classifyTriangle(10, 30, 30), 'Isoceles','30+30= 60 > 10 and it is isoceles')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(4, 5, 6),'Scalene', '4,5,6 equals scalene')
        self.assertNotEqual(classifyTriangle(4,5,4),'Scalene','4,5,4 not a scalene')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

