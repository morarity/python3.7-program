class Grade:
	
	def my_program():
		""" a simple program for calculating grades in python
		"""
		pass
	
	#instances
	def __init__(self, score):
		self.score = int(score)

	# grade calculation elif functions.
	def isscore(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 80:
			return 'B'
		elif self.score >= 70:
			return 'C'
		elif self.score >= 60:
			return 'D'
		else:
			return 'F'

print(Grade.my_program.__doc__)
name = Grade(input('Put your grade here: ')) # the example grade.

if __name__ == '__main__':
	print(name.score)
	print(name.isscore())