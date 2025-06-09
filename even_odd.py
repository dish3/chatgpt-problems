n=input("Enter the number of rows: ")
even=0
odd=0

for i in n:
    if i.isdigit():
        if int(i)%2==0:
            even+=1
        else:
            odd+=1
print("Even numbers:", even)
print("Odd numbers:", odd)