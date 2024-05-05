import sys
n=int(sys.stdin.readline())
dic={}

for i in range(n):
    a,b=sys.stdin.readline().split()
    if b == "enter":
        dic[a]=b
    elif b == "leave" and a in dic:
        del dic[a]

sorted_dict = sorted(dic,reverse=True)
for i in sorted_dict:
    print(i)