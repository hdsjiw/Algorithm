import sys

input = sys.stdin.readline

n = int(input())
mod = 1000000007

# (F(n), F(n+1))을 반환하는 함수
def fib(n):
    if n == 0:
        return (0, 1)
    
    a, b = fib(n // 2)
    
    c = (a * ((2 * b - a) % mod)) % mod  # 짝수 번째 계산 F(2k)
    d = (a * a + b * b) % mod            # 홀수 번째 계산 F(2k+1)
    if n % 2 == 0:
        return (c, d)
    else:
        return (d, (c + d) % mod) # (c + d): F(n - 1) + F(n - 2)

print(fib(n)[0])
