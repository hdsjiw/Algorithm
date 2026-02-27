A = input()

# Please write your code here.
answer=0

for i in range(len(A)):
    if A[i]=='(':
        tem=A[i+1:len(A)]
        answer+=tem.count(')')
print(answer)