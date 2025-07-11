text = input()
pattern = input()

# Please write your code here.
def find_char(text):
    index=text.find(pattern)
    return index

index=find_char(text)
print(index)