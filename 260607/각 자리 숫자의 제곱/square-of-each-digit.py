N = int(input())

# Please write your code here.
def f(N):
    if N < 10:
        return N * N

    digit = N % 10
    return f(N // 10) + digit * digit

print(f(N))

