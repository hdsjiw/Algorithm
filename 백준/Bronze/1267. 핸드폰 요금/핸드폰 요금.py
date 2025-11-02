import sys

n = int(input())
time = list(map(int, input().split()))
y = m = 0
for n in time:
    y += (n//30 + 1) * 10
    m += (n//60 + 1) * 15
if m == y:
    print("Y M", m)
elif m < y:
    print("M", m)
else:
    print("Y", y)
   
    