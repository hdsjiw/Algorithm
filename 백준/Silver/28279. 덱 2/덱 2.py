import sys
from collections import deque
n=int(sys.stdin.readline())
deque = deque([])

for i in range(n):
    a=sys.stdin.readline().split()
    if a[0]=='1':
        deque.appendleft(a[1]) # 덱의 앞에 넣기
    elif a[0]=='2':
        deque.append(a[1])
    elif a[0]=='3':
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif a[0]=='4':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif a[0]=='5':
        print(len(deque))
    elif a[0]=='6':
        if deque:
            print(0)
        else:
            print(1)
    elif a[0]=='7':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif a[0]=='8':
        if deque:
            print(deque[-1])
        else:
            print(-1)