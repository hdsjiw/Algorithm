k=int(input())
for i in range(k):
    grades = list(map(int, input().split()))
    grades.pop(0)
    grades.sort(reverse=True)
    dif=set()
    for j in range(len(grades)-1):
        dif.add(grades[j]-grades[j+1])
    print(f"Class {i+1}")
    print(f"Max {max(grades)}, Min {min(grades)}, Largest gap {max(dif)}")