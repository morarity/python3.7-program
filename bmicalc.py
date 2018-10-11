#instances.
def is_overweight():
	weight = input('Your weight in kilograms: ')
	height = input('Your height in meters: ')
	kg = int(weight)
	tall = float(height)
	bmi = (kg / tall) / tall
	print(bmi)

	if bmi <= 18.5:
		 print('Underweight')
	elif bmi <= 24.9:
		 print('Normal Weight')
	elif bmi <= 29.9:
		 print('Overweight')
	elif bmi <= 30:
		 print('Obesity')
	else:
		 print('Not Defined likely Obese')

	print('The normal weight is 24.9')

if __name__ == '__main__':
	is_overweight()
	