import sys

input = sys.stdin.readline

n, m = map(int, input().split())

num_to_name = {}
name_to_num = {}

for i in range(1, n+1):
    name = input().rstrip()
    num_to_name[i] = name
    name_to_num[name] = i

for _ in range(m):
    tem = input().rstrip()
    if tem.isdigit():
        print(num_to_name[int(tem)])
    else:
        print(name_to_num[tem])
