integers=list(map(int,input().split()))
sum_2=0
num_2=0
for integer in integers:
    if integer==0:
        break
    else:
        if integer%2==0:
            sum_2+=integer
            num_2+=1
print(num_2,sum_2,sep=" ")