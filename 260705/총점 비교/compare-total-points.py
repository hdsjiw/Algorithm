n = int(input())

name = []
score1 = []
score2 = []
score3 = []

class Student():
    def __init__(self,name,score1,score2,score3):
        self.name=name
        self.score1=score1
        self.score2=score2
        self.score3=score3

students=[]

for _ in range(n):
    student_info = input().split()
    student=Student(student_info[0],int(student_info[1]),int(student_info[2]),int(student_info[3]))
    students.append(student)

# Please write your code here.
students.sort(key=lambda x: x.score1+x.score2+x.score3 )

for student in students:
    print(student.name, student.score1, student.score2,student.score3)
    