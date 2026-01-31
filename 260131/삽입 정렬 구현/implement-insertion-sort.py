n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(1, n):
    j = i
    while j > 0 and arr[j-1] > arr[j]:
        arr[j-1], arr[j] = arr[j], arr[j-1]
        j -= 1


print(*arr)