n=int(input())
for i in range(n):
    a=list(map(int,input().split()))
    avg=(sum(a[1:])/a[0])
    pct=0
    for i in range(a[0]):
        if a[i+1]>avg:
            pct+=1
    pct=(pct/a[0])*100
    print("{:.3f}%".format(pct))
