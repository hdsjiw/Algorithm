n=int(input())
stairs=[]
for i in range(n):
    stair_score=int(input())
    stairs.append(stair_score)
    
score_sum=[]
if n==1:
    print(stairs[0])
elif n==2:
    print(sum(stairs))
elif n==3:
    print(stairs[-1]+max(stairs[0],stairs[1]))
else: #n>=4
    score_sum.append(stairs[0])
    score_sum.append(stairs[0]+stairs[1])
    score_sum.append(stairs[2]+max(stairs[0],stairs[1]))
    
    for i in range(3,n):
        score_sum.append(stairs[i] + max(stairs[i-1] + score_sum[i-3], score_sum[i-2]))

    print(score_sum[n-1])