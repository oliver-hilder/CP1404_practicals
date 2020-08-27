"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur if either the variable "numerator" or "denominator" receive input that is not an integer.
2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur if the user enters the value "0" into the variable "denominator"
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
By changing the "denominator" input to a small while loop to avoid "0" input, the ZeroDivisionError can be avoided.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Error. Denominator value cannot be zero.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")