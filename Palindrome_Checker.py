n=input("enter a string: ")
n=n.lower()
def ip(n1):
    n1=n1[::-1]
    if n1==n:
        print("it is a palindrome")
    else:   
        print("it is not a palindrome")
ip(n)