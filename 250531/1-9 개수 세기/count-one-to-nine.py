count_arr=[0]*10

# 개수 세기
n=int(input())
arr=list(map(int,input().split()))
for elem in arr:
    count_arr[elem]+=1

for i in range(1,10):
    print(count_arr[i])