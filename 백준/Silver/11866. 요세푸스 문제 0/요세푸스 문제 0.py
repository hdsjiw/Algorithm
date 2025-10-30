import sys

n,k=map(int, sys.stdin.readline().split())

people=[i+1 for i in range(n)]
result=[]
index=0
while people:
    index = (index + k - 1) % len(people)  # k번째 사람 인덱스 계산
    result.append(people.pop(index))        # 제거된 사람을 결과에 추가

print("<" + ", ".join(map(str, result)) + ">")