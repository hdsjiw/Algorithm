import sys
import re
n=int(sys.stdin.readline())
stack=[]

for i in range(n):
    order=sys.stdin.readline().split()
    if 'push' in order:
        num=""
        for char in order:
            if char.isdigit():  # 문자가 숫자인지 확인
                num += char  # 숫자라면 결과 문자열에 추가
        stack.append(num)
    elif 'pop' in order:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif 'size' in order:
        print(len(stack))
    elif 'empty' in order:
        if stack:
            print(0)
        else:
            print(1)
    else: #a[0]=='5'
        if stack:
            print(stack[-1])
        else:
            print(-1)