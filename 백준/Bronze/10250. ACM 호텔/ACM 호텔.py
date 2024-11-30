import sys

t=int(sys.stdin.readline())
for i in range(t):
    h,w,n = map(int, sys.stdin.readline().split())
    floor = n % h
    room = n // h + 1
    if floor == 0:
        room -= 1
        floor = h
 
    print(floor*100 + room)
