e,s,m=map(int,input().split())
year=0
i=j=k=0

while True:
    i+=1
    j+=1
    k+=1

    year+=1

    if i>15:
        i=1
    if j>28:
        j=1
    if k>19:
        k=1

    if e==i and s==j and m==k:
        print(year)
        break

