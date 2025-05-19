s_list=list(map(str,input().split()))
s_list_slicing=s_list[1::3]
for s in s_list_slicing:
    print(s,end=" ")