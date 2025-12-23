import sys
input = sys.stdin.readline

n,k=map(int,input().split())
per=[i for i in range(1,n+1)]

idx = 0
result = []

while per:
    idx = (idx + k - 1) % len(per)
    result.append(per.pop(idx))

print("<" + ", ".join(map(str, result)) + ">")
