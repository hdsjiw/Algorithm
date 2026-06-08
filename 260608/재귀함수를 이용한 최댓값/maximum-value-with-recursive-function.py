n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def find_max(n):
    if n == 1:
        return arr[0]

    return max(find_max(n - 1), arr[n - 1])

print(find_max(n))