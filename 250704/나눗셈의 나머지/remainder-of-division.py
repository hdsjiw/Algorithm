A,B=map(int,input().split())
arr=[0]*B

while A>1:
    share=A%B
    A=A//B
    arr[share]+=1

ans=0
for i in range(len(arr)):
    ans+=arr[i]**2

print(ans)
