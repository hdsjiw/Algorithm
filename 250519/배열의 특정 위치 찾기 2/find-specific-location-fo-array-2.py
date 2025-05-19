n_list=list(map(int,input().split()))
odd_list=n_list[::2]
even_list=n_list[1::2]
sum_odd=sum(odd_list)
sum_even=sum(even_list)
if sum_odd>sum_even:
    print(sum_odd-sum_even)
else:
    print(sum_even-sum_odd)