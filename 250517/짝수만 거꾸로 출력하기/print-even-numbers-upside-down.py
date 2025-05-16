n=int(input())
num_list=list(map(int,input().split()))
num_list2=[] # 2의 배수만 저장하는 리스트
for num in num_list:
    if num%2==0:
        num_list2.append(num)

for num in num_list2[::-1]:
    print(num,end=" ")