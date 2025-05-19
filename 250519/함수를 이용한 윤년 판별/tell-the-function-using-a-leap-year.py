y = int(input())

# Please write your code here.
def is_yunyeon(year):
    if year%4==0:
        if year%100==0 and year%400!=0:
            return False
        else:
            return True
    else:
        return False

if is_yunyeon(y):
    print("true")
else:
    print("false")