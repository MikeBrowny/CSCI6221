'''
PL: ch9, 10

Homework Question: 40 pts

Write a program/function in any programming language that will implement Calling Subprograms Indirectly as discussed on the slides of ch9.

Your program/function will take 2 non-zero, positive integers, e.g., 6 and 12 OR 16 and 2, as input parameters, and output any prime numbers between these 2 inputs.  

e.g.,

> printPrime 40 31

31 is a prime number

37 is a prime number

> printPrime  31  40

31 is a prime number

37 is a prime number

> printPrime   230   240

233 is a prime number

239 is a prime number

> printPrime  231  245

233 is a prime number

239 is a prime number

241 is a prime number

Please DO NOT hard-code any input values, output values in your code.

'''

import math

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def process_numbers(start, end, callback):
    """Process numbers between start and end using the provided callback function."""
    if start > end:
        start, end = end, start
    for num in range(start, end + 1):
        callback(num)

def print_prime(num):
    """Print the number if it is prime."""
    if is_prime(num):
        print(f"{num} is a prime number")

# Get input from user
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

# Call the function with user input
process_numbers(start, end, print_prime)

'''

Enter the start number: 
40
Enter the end number: 
31
31 is a prime number
37 is a prime number


** Process exited - Return Code: 0 **
Press Enter to exit terminal

'''