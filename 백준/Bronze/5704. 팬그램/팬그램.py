alphabets =[chr(i) for i in range(97,123)]
while True:
    case=input()
    if case=="*":
        break
    else:
        pangram=True
        for alphabet in alphabets:
            if alphabet not in case:
                pangram=False
                print("N")
                break

        if pangram:
            print("Y")