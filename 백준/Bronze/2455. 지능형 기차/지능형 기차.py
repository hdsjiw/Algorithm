import sys

max_people=0
in_people=0
for _ in range(4):
    a,b=map(int, sys.stdin.readline().split())
    in_people += b - a
    max_people = max(max_people, in_people)
print(max_people)
