n=int(input())
n_list=list(map(int,input().split()))
even_list=[]
for num in n_list:
    if num%2==0:
        even_list.append(num)

for num in even_list:
    print(num,end=" ")