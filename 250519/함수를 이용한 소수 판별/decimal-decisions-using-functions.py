a, b = map(int, input().split())

# Please write your code here.
sum_prime=0
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

    
for i in range(a,b+1):
    if is_prime(i):
        sum_prime+=i

print(sum_prime)