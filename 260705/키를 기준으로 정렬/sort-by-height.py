n = int(input())

class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

people = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    person = Person(n_i, int(h_i), int(w_i))
    people.append(person)

people.sort(key=lambda x: x.height)

for person in people:
    print(person.name, person.height, person.weight)
    