n_list=list(map(int,input().split()))

n2_list=n_list[1::2]
n3_list=n_list[2::3]
avg=sum(n3_list)/len(n3_list)

print(f"{sum(n2_list)} {avg:.1f}")