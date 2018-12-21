print('-'*80)
print('Narrative Bot:')
print()


student = input('Student Name: ')
grade = input('Grade: ')
grade = int(grade)

if grade >= 65:
	print('Narrative: Congrats! You have passed this class! You are going to Heaven!')
else grade <= 65:
	print('Narrative: Shame! You have failed this class! Prepare to meet Satan in hell!')