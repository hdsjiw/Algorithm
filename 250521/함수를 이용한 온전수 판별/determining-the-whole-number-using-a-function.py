a, b = map(int, input().split())

# Please write your code here.
num=0

def discrimination(n):
    if perfact_num(n):
        return False
    else:
        return True
        
def perfact_num(n):
    return (n%2==0) or (n%10==5) or ((n%3==0) and (n%9==0))


for i in range(a,b+1):
    if discrimination(i):
        num+=1

print(num)