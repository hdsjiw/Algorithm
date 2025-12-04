import sys

input=sys.stdin.readline

n=int(input())
n_list=list(map(int, input().split()))
max_n=max(n_list)
min_n=min(n_list)
print(max_n*min_n)
