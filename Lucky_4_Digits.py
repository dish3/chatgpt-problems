def is_lucky(a,b):
    found = False
    for i in range(a,b+1):
        if i%7==0:
            digits= str(i)
            if len(digits)==4 and len(set(digits))==4:
                found = True
                print(i)
    if not found:
        print("No lucky numbers found in the range.")
    a,b=map(int, input("Enter the range (a b): ").split())
    is_lucky(a,b)