n=int(input())
length=list(map(int,input().split()))

sum_len=sum(length)
cost=0

for i in range(len(length)-1):
    sum_len-=length[i]
    cost+=sum_len*length[i]

print(cost)