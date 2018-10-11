# grade calculation elif functions.
def is_score():
	grade = input('Enter your grade here: ')
	grade = int(grade)
	if grade >= 90:
		print('A')
	elif grade >= 80:
		print('B')
	elif grade >= 70:
		print('C')
	elif grade >= 60:
		print('D')
	else:
		print('F')

#execution of program
if __name__ == '__main__':
	is_score()