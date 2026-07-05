n = 5

class Person():
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight

people=[]

for _ in range(n):
    n, h, w = input().split()
    person=Person(n,int(h),float(w))
    people.append(person)

# Please write your code here.
people.sort(lambda x:x.name)

print("name")
for person in people:
    print(person.name,person.height,person.weight)

print()
people.sort(lambda x:-x.height)

print("height")
for person in people:
    print(person.name,person.height,person.weight)