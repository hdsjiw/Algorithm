def mode_num(nums):
    keys=set(nums)
    count=dict.fromkeys(keys,0)
    max_list=[]
    
    for i in nums:
        count[i]+=1

    #print(count)
        
    # 최빈값 찾기
    max_freq = max(count.values())
    modes = [k for k, v in count.items() if v == max_freq]
    
    if len(modes) > 1:
        return sorted(modes)[1]  # 최빈값이 여러 개일 때 두 번째로 작은 값 반환
    else:
        return modes[0]

n=int(input())
nums=[]
for i in range(n):
    num=int(input())
    nums.append(num)

average=sum(nums)/len(nums)

sort_num=sorted(nums)
mid=sort_num[int(len(nums)/2)]

mode=mode_num(nums)
ran=max(nums)-min(nums)

print(round(average))
print(mid)
print(mode)
print(ran)
