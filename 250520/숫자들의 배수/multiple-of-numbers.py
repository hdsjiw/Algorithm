n=int(input())
i=1
mul_5=0
while True: 
    if mul_5==2:
        break
    
    tem=n*i

    if tem%5==0:
        mul_5+=1

    print(tem,end=" ")
    i+=1

    