a, b = map(int, input().split())

# Please write your code here.
num=0
    
def perfact_num(n):
    return (n%2==0) or (n%10==5) or ((n%3==0) and (n%9==0))

def perfact_num2(n):
    return (n%2!=0) and (n%10!=5) and ((n%3!=0) or (n%9==0))

for i in range(a,b+1):
    if perfact_num2(i):
        num+=1
print(num)