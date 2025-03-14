n=int(input())
length=list(map(int,input().split()))
sum_len=sum(length)
cost=0

for i in range(n-1):
    x=min(length)
    length.remove(x)
    sum_len-=x
    cost+=sum_len*x

print(cost)