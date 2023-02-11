"""
Assignment 01
@author: Darshan Bhanushali
"""

from datetime import datetime

class Triangle:
	def my_brand(self):
		today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		info ="""
		=*=*=*= Darshan Bhanushali =*=*=*=
		=*=*=*= Course 2023S-SSW567-WS =*=*=*= 
		=*=*=*= HW 01 - Triangles =*=*=*= 
		"=*=*=*="""+today+"""=*=*=*="
		"""
		print(info)
		
		
	def classify_triangle(self,a, b, c):
		if a == 0 or b == 0 or c == 0:
			return 'Invalid Triangle'
		if a == b and b == c and a == c:
			return "equilateral"
		else:
			lst = [a, b, c]
			lst.sort()
			if lst[0] + lst[1] <= lst[2]:
				return "Invalid Triangle"
			if lst[0] == lst[1] or lst[1] == lst[2]:
				return "isoceles"
			elif lst[0]**2 + lst[1]**2  == lst[2]**2:
				return "right"
			else:
				return 'scalene'
			
	def __init__(self):
		self.message = "Hello world"

if __name__ == '__main__':
	triangle = Triangle()
	print(triangle.classify_triangle(4,5,6))