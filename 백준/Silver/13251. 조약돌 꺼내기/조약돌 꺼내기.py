m=int(input())
n=list(map(int,input().split()))
k=int(input())

den=1
mol=0
val=sum(n)

for i in range(k): #분모
    den*=val
    val-=1
#print(den)
#print()

#print(n)
#print()

for i in n: #분자
    mol_val=1
    val=i
    for j in range(k):
        mol_val*=val
        #print("val")
        #print(val)
        val-=1
    #print(mol_val)
    mol+=mol_val
    
#print(mol)

print(mol/den)
