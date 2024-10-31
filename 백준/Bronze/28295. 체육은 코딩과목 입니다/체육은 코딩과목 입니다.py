direction=["N","E","S","W"]
n=0
for i in range(10):
    t=int(input())

    if t==1:
        n+=1
    elif t==2:
        n+=2
    else:
        n-=1
        
if n%4==0:
    print(direction[0])
elif n%4==1:
    print(direction[1])
elif n%4==2:
    print(direction[2])
else:
    print(direction[3])