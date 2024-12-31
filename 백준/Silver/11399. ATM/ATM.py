n=int(input())
time=list(map(int,input().split()))
t=0
sum=0
time.sort()
for i in range(len(time)):
    t+=time[i]
    sum+=t
print(sum)