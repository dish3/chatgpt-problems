"""
🧩 Problem Statement:
You are given a number n. Print numbers from 1 to n with the following rules:

If a number is divisible by 3, print "Fizz"

If it's divisible by 5, print "Buzz"

If it's divisible by both 3 and 5, print "FizzBuzz"

Otherwise, just print the number


"""

n=int(input("Enter a number: "))

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)