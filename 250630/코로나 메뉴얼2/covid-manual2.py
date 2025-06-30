med=[0]*4

for i in range(3):
    state,temp=input().split()
    temp=int(temp)

    if state=="Y" and temp>=37:
        med[0]+=1
    elif state=="N" and temp>=37:
        med[1]+=1
    elif state=="Y" and temp<37:
        med[2]+=1
    else:
        med[3]+=1

if med[0]>=2:
    med.append("E")

for elm in med:
    print(elm,end=" ")