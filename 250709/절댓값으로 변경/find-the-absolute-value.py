n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def absolute(arr):
    for num in arr:
        num=abs(num)
        print(num,end=" ")

absolute(arr)