a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.

def operation(a,o,c):
    if o=="+":
        return(a+c)
    elif o=="-":
        return(a-c)
    elif o=="*":
        return(a*c)
    elif o=="/":
        return(int(a/c))
    else:
        return "False"

print(f"{a} {o} {c} = {operation(a,o,c)}")
