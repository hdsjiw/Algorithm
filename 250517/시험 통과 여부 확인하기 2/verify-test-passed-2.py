st_num=int(input())
pass_num=0
for i in range(st_num):
    grade=list(map(int,input().split()))
    avg=sum(grade)/4
    if avg>=60:
        print("pass")
        pass_num+=1
    else:
        print("fail")
print(pass_num)