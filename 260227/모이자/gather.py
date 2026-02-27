n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
min_val=0
for i in range(n):
    distance=0
    for j in range(n):
        distance+=A[j]*abs(i-j)
    if min_val==0:
        min_val=distance
    else:
        min_val=min(min_val,distance)

print(min_val)
