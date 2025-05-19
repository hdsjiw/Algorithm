a, b = map(int, input().split())
num=0

# Please write your code here.
def magic_num(n):
    return n%3==0 or contain_num(n)


def contain_num(n):
    n1=n//10
    n2=n%10
    return (n1==3) or (n1==6) or (n1==9) or(n2==3) or (n2==6) or (n2==9)



for i in range(a,b+1):
    if magic_num(i):
        num+=1
print(num)