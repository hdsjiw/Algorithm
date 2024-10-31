while True:
    n = input()  
    if n == "0":
        break

    palin = True
    for i in range(len(n) // 2):
        if n[i] != n[len(n) - i - 1]:
            palin = False
            print("no")
            break
    
    if palin:
        print("yes")

