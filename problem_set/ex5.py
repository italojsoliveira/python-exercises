# Write a program that receives two student grades and outputs the average grade.

grade_1 = float(input('Enter the first grade: '))

grade_2 = float(input('Enter the second grade: '))

print('The first student grade is {}.'.format(grade_1))

print('The second student grade is {}.'.format(grade_2))

print('The average between {} and {} is {}'.format(grade_1, grade_2, (grade_1 + grade_2)/2))