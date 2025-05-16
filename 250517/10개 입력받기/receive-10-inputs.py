integers=list(map(int,input().split()))
sum1=0
avg=0
n=0

for integer in integers:
    if integer==0:
        break
    else:
        sum1+=integer
        n+=1

avg=sum1/n
print(f"{sum1} {avg:.1f}")