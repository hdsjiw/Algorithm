n=int(input())
n_list=list(map(int,input().split()))
new_list=[num**2 for num in n_list]
for num in new_list:
    print(num, end=" ")