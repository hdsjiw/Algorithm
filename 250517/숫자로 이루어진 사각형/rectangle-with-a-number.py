n = int(input())

# Please write your code here.
def print_rectange(n):
    num=0
    for i in range(n):
        for j in range(n):
            num+=1
            if num>9:
                num=1
            print(num,end=" ")
        print()
    
print_rectange(n)