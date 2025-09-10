print("This is Day 4")

"""Basic Calculator Function
Write a function calculator(a, b, operation) that:
Supports add, subtract, multiply, divide.
Example:calculator(10, 5, "add")  # → 15
calculator(10, 5, "divide")  # → 2
Add error handling for division by zero.
"""

def calulator(a: int , b: int , operations : str ):
    if operations ==  "add":
        return (a + b)
    elif operations == "subtract":
        return a - b
    elif operations == "multiply":
        return a * b
    elif operations == "divide":
        if b == 0 :
            return "Error: Division by 0 "
        else:
            return a / b
    else:
        return "Error: Invalid operation"

print(calulator(10, 15, "subtract"))  # → 15


"""Mean & Median Function
Write a function my_mean(numbers) → returns the average.
Write a function my_median(numbers) → returns the median (handle both even & odd list lengths)."""

def my_mean(numbers: list):
    return sum(numbers)/len(numbers)
def my_median(numbers: list):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 ==0:
         median = (numbers[mid - 1 ]+ numbers[mid]) // 2
    else:
        median = numbers[mid]
    return median
print(my_mean([1, 2, 3, 4, 5]))
print(my_median([100, 22, 43, 4, 15]))

def variance(numbers : list):
    sample_mean = my_mean(numbers)
    n = len(numbers)
    top = 0
    for i in range(n):
        top += (numbers[i] - sample_mean) ** 2
    return top / (n-1)
print(variance([1, 2, 3, 4, 5]))

import math
sttandard_deviattion = math.sqrt(variance ([1, 2, 3, 4, 5]))
print(sttandard_deviattion)
