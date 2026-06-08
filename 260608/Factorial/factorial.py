N = int(input())

# Please write your code here.
def fac(N):
    if N==1:
        return 1
    return fac(N-1)*N

print(fac(N))