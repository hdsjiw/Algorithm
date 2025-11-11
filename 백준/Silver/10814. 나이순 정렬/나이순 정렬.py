import sys

n=int(sys.stdin.readline().strip())
member=[]

for _ in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    member.append([age,name])

sorted_member = sorted(member, key= lambda x : x[0])

for age,name in sorted_member: # 출력 코드
    print(age,name)
