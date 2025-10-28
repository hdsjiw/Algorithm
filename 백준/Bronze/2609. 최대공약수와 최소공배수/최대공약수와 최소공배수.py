import sys

def gcd(n, m): # 최대공약수
    while m > 0:
        n, m = m, n % m
    return n

def lcm(n, m):  # 최소공배수
    return n // gcd(n, m) * m

n,m=map(int, sys.stdin.readline().split())
print(gcd(n,m))
print(lcm(n,m))
