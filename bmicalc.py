class OverWeight: # class.

	def my_program():
		"""A simple program to calculate body mass index
		"""
		pass

	#instances.
	def __init__(self, kg, tall):
		self.kg = int(kg)
		self.tall = float(tall)
		self.bmi = float(self.kg / self.tall) / 1.75


	#bmi calculator elif functions.
	def isoverweight(self):
		if self.bmi <= 18.5:
			return 'Underweight'
		elif self.bmi <= 24.9:
			return 'Normal Weight'
		elif self.bmi <= 29.9:
			return 'Overweight'
		elif self.bmi > 30:
			return 'Obesity'
		else:
			return 'Not Defined'

			
print(OverWeight.my_program.__doc__)

name = OverWeight(input('Put your weight in kilogram: '), input('Put your height in meter: ')) # your height and Weight

if __name__ == '__main__':
	print('Your bmi is {}'.format(name.bmi))
	print('Your weight is {}'.format(name.isoverweight()))
	