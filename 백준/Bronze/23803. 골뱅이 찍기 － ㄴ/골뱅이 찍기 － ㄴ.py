n=int(input())
for i in range(5):
    if i==4:
        for j in range(n):
            for k in range(n*5):
                print("@",end="")
            print()
    else:
        for j in range(n):
            for k in range(n):
                print("@",end="")
            print()