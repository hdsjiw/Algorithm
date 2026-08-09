n = int(input())

def star(x):
    print("* " * x)

    if x == 1:
        print("*")
        return

    star(x - 1)

    print("* " * x)

star(n)