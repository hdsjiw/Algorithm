n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
def print_nums(nums):
    for num in nums:
        print(num,end=" ")
    print()
    
nums.sort()
print_nums(nums)
nums.sort(reverse=True)
print_nums(nums)