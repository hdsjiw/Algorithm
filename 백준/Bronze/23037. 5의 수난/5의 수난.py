n=input()
n_list=list(map(int,str(n)))
sum1=0
for i in n_list:
    sum1+=i**5
print(sum1)