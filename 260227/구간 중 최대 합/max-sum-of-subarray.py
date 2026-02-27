n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
max_val=0

for i in range(n-k):
    tem=arr[i:i+k]
    sum_tem=sum(tem)
    
    max_val=max(max_val,sum_tem)
print(max_val)