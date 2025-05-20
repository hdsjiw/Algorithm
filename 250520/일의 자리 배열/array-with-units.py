a,b=map(int,input().split())
arr=[a,b]
for i in range(2,10):
    tem=arr[i-1]+arr[i-2]
    arr.append(tem)

# 출력
for num in arr:
    print(num%10,end=" ")
