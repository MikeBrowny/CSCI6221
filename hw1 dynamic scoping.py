# PL: ch5
# Homework Questions:
# Write a function in any programming language that will demonstrate dynamic scoping. The function should be executable. Please indicate what’s the programming language used in your answer.  [pl_ch5: scope 20 pts]


def outer_function():
    x = 1
    
    def inner_function():
        global x
        print("Inside inner_function:", x)
    
    inner_function()
    print("Inside outer_function:", x)

outer_function()