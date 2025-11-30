import sys

input=sys.stdin.readline
x=int(input())
line = 1

while x > line:
    x -= line
    line += 1
    
# 짝수
if line % 2 == 0:
    a = x
    b = line - x + 1

# 홀수
elif line % 2 == 1:
    a = line - x + 1
    b = x

print(f'{a}/{b}')
