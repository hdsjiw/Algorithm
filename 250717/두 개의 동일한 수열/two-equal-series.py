n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A.sort()
B.sort()

state=False

for i in range(n):
    if A[i]==B[i]:
        state=True
    else:
        state=False
        break

if state:
    print("Yes")
else:
    print("No")