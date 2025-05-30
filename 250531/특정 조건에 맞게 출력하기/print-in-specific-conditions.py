n_list=list(map(int,input().split()))

for i in range(len(n_list)):
    if n_list[i]==0:
        break
    
    elif n_list[i]%2!=0:
        print(n_list[i]+3,end=" ")
    else:
        print(n_list[i]//2,end=" ")
