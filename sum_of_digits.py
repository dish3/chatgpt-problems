n = int(input("Enter a number: "))

def sumd(n1):
    total = 0
    for i in str(n1):     
        total += int(i)    
    return total

print("Sum of digits is:", sumd(n))
