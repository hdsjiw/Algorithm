n=int(input())
n_list=[1,n]

num=0
i=0

while num<=100:
    num=n_list[i]+n_list[i+1]
    n_list.append(num)
    i+=1

for i in n_list:
    print(i,end=" ")