import sys

odd_list=[]
for _ in range(7):
    n=int(sys.stdin.readline())
    if n%2==1:
        odd_list.append(n)

if odd_list:
    print(sum(odd_list))
    print(min(odd_list))
else:
    print(-1)
