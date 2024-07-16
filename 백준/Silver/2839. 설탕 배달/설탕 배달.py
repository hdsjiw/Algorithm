n=int(input())
num=0

if n%5==0:
    print(n//5)
else:
    num+=(n//5)
    n5=n%5
    if n5%3==0: #그대로 진행
        num+=(n5//3)
        print(num)
    else:
        while True:
            if n5>=n:
                print(-1)
                break
            
            n5+=5
            num-=1
            if n5%3==0:
                num+=(n5//3)
                print(num)
                break
