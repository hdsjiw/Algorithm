n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
arr=[]
#각각 양끝에 있는 요소끼리 묶으면 최댓값이 최소가 됨
for i in range(n):
    arr.append(nums[i]+nums[-1-i])
print(max(arr))
    
