student = {"name" : "yashwanth", "age" : 19 , "courses" : {"DBMS", "CA"}}
print(student.get("phone","note found")) 

student['phone'] = '555-5555'
student['name'] = 'Jane'

print(student['phone'])

student.update({'name': 'Jane', 'age' : 44, 'sex' : 'M'})
print(student)

# del student['age']
# print(student)

age = student.pop('age')
print(student)
print(age)

print(len(student))

print(student.values())

print(student.keys())

print(student.items())

for key in student:
    print(key)

for key, value in student.items():
    print(key, value)