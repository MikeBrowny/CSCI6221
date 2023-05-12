'''
PL: ch7, 8

Homework Question: 80 pts

Write a program/function in any programming language that will implement Loop Guarded Command (LGC) as discussed on the last slide of ch8.

Your program/function will take 3 non-zero, positive integers, e.g., 3, 6, and 12.  Please note that your code should be able to take different values other than 3, 6, and 12.

The first two input integers should have different values, e.g., 3 and 6. These 2 integers will be used to create a range of integers (e.g., from 3 to 6), which will be used to create a list of Boolean expressions as follows:

    the first Boolean expression will be defined as “x%3 == 0”, i.e., to check if x%3 has 0 remainder.  
    the second Boolean expression will be defined as “x%4 ==0”
    the third Boolean expression will be defined as “x%5==0”
    The last Boolean expression will be defined as “x%6==0”

  where variable x will take the third input integer as explained below.

 

The statement corresponding to each Boolean expression defined above will print out the Fibonacci numbers that are less than the integer used in the Boolean expression.  E.g., the statement for the second Boolean expression x%4==0 will print out “0 1 1 2 3”; for the fourth Boolean expression x%6==0 will print out “0 1 1 2 3 5”.

The third input integer to your program/function will be used as input value for variable x defined in the Boolean expressions above.  E.g., if the third input integer is 12, the first, second, and fourth Boolean expressions will have a true value (i.e., 12%3 = 12%4 = 12%6 = 0). The LGC will randomly, non-deterministically choose ONE of 3 corresponding statements to print out the Fibonacci numbers, as described above.

If the third input integer to your program function failed all Boolean expressions defined, your program should throw runtime errors and be terminated.

Please DO NOT hard-code any input values, output values in your code.

'''

import random

def fibonacci(n):
    fib_seq = [0, 1]
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:-1]

def lgc_program():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    x = int(input("Enter the third number: "))

    if a == b:
        raise ValueError("The first two input integers must have different values.")

    int_range = list(range(min(a, b), max(a, b) + 1))
    bool_exprs = [x % i == 0 for i in int_range]

    if any(bool_exprs):
        selected_expr = random.choice([i for i, expr in enumerate(bool_exprs, start=min(a, b)) if expr])
        fib_nums = fibonacci(x)
        print("Fibonacci numbers less than", x, ":")
        print(*fib_nums[:selected_expr + 1])
    else:
        raise ValueError("No Boolean expression is True.")

# Example usage
lgc_program()



'''
Enter the first number: 
3
Enter the second number: 
6
Enter the third number: 
12
Fibonacci numbers less than 12 :
0 1 1 2 3 5 8


** Process exited - Return Code: 0 **
Press Enter to exit terminal
'''