N = int(input())

# Please write your code here.
num=0 # 진행한 작업의 횟수

def f(N):
    if N==1:
        return 0
    if N%2==0:
        return f(N//2)+1
    else:
        return f(N//3)+1
print(f(N))