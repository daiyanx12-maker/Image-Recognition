#class creation
class student:
    name = ''
    id = ''
    age = ''
    grade = ''
    school = ''
    GPA = ''

# Object creation
s1 = student()
s1.name = 'daiyan'
s1.age = 13
s1.id = 20
s1.grade = 7
s1.school = "KCABN"
s1.GPA = '4.5'

print(f"Name: {s1.name} \nAge: {s1.age} \nId: {s1.id} \ngrade: {s1.grade} \nSchool: {s1.school} \nGPA: {s1.GPA}")
print(isinstance(s1,student))
n = 'daiyan'
c = 10
print(f"My name is {n} and my age is {c}")