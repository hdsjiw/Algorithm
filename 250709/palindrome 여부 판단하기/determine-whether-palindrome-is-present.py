A = input()

# Please write your code here.
def paindrome(A):
    A_list=list(A)
    A_list.reverse()
    A_reverse = ''.join(A_list)
    if A==A_reverse:
        return "Yes"
    else:
        return "No"

print(paindrome(A))