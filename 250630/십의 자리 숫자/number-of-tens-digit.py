arr=list(map(int,input().split()))

count_arr=[0]*10

# 개수 세기
for elem in arr:
    if elem==0:
        break
    elem=elem//10
    count_arr[elem]+=1

for i in range(1,10):
    cnt=count_arr[i]
    print(f"{i} - {cnt}")