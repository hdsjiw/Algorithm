arr=list(map(int,input().split()))

count_arr=[0]*11

# 개수 세기
for elem in arr:
    if elem==0:
        break
    elem=elem//10
    count_arr[elem]+=1

# 역순 출력
for i in range(10, 0, -1):
    cnt = count_arr[i]
    print(f"{i * 10} - {cnt}")