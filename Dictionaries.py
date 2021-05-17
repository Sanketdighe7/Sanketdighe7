student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
student_phone = '+919765561312'
student_name = 'Sanket'

student.update({'name': 'Sanket', 'age': '24', 'Phone': '+919765561312'})
print(student)
# popped = student.pop('age')
# print(popped)
# or
del student['age']
print(student)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)
