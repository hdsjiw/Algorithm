a1,a2=map(int,input().split())
a_list=[a1,a2]
for i in range(10-2):
    num=a_list[i+1]+2*a_list[i]
    a_list.append(num)

for num in a_list:
    print(num,end=" ")
