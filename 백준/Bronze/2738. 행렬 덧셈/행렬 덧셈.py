n,m=map(int,input().split())
arr=[]
arr2=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
    
for i in range(n):
    arr2.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(m):
        arr[i][j]+=arr2[i][j]
        print(arr[i][j],end=" ")
    print()