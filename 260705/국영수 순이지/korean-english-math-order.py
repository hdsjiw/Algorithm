n = int(input())
name = []
korean = []
english = []
math = []

class Student():
    def __init__(self,name,korean,english,math):
        self.name=name
        self.korean=korean
        self.english=english
        self.math=math

students=[]

for _ in range(n):
    student_info = input().split()
    student=Student(student_info[0],int(student_info[1]),int(student_info[2]),int(student_info[3]))
    students.append(student)

# Please write your code here.

students.sort(key=lambda x: (-x.korean,-x.english,-x.math))

for student in students:
    print(student.name, student.korean, student.english,student.math)
    