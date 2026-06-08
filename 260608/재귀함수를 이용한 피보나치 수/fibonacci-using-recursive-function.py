N = int(input())

# Please write your code here.
def fib(N):
    if N==1:
        return 1
    if N==2:
        return 1
    return fib(N-1)+fib(N-2)

print(fib(N))