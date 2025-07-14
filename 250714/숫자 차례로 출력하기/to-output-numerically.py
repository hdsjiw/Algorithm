n = int(input())

# Please write your code here.
def print_num(n):
    if n==0:
        return

    print(n,end=" ")
    print_num(n-1)

def print_num2(n):
    if n==0:
        return

    print_num2(n-1)
    print(n,end=" ")

print_num2(n)
print()
print_num(n)
