a=list(map(int,input().split()))
sum1=0
avg=0
n=0

for i in range(len(a)):
    if a[i]>=250:
        n=i
        break
    else:
        sum1+=a[i]
        n=i+1
avg=sum1/n


print(sum1,avg,sep=" ")