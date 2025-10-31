n=int(input())
n_list = list(map(int, str(n)))
n_list.sort(reverse=True)
for num in n_list:
    print(num,end="")