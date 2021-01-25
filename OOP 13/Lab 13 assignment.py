

'''
Task1:
Write a program that take a user input to catch an exception of ZeroDivisionError.
and Value Error

'''

try: 
    
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    print(x/y)

except ValueError:
    print("\nError: Please enter an integer value.")

except ZeroDivisionError:
    print("\nError: Division by zero.")


'''
Task2:

Write a program that take a user input to catch an exception of TypeError.

'''

try:
    
    n1 = input("Enter first number: ")
    n2 = input("Enter second number: ")
    res = print(n1/n2)
    
except TypeError:
    print("\nError: Incorrect type of input.")







