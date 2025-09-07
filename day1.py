print("This is Day 1")
print ("Today I'll be working on basic python programming concepts.")

# Reverse a string
def reverse_string(str: str):
    return str[::-1]

print(reverse_string('Hello_World'))
"""string = input("Enter a string you want to reverse:")
out = reverse_string(string)
print(out)
"""
# Factorial of a number
## factorial of a number by recursion
def factorial(n: int):
    if n == 1 or 0:
        return 1

    for i in range(1,n):
        n = n * i
        i = i -1
    return n

print (factorial(5))

## factorial of a number by factorial function from math module
import math

def factorial_func(n: int):
    return math.factorial(n)

print (factorial_func(2))

"""1. Sales Tracker (Lists + Loops + Functions)
Create a list of 10 sales amounts (any numbers you want).
Write a function that:
Returns the total sales.
Returns the average sale.
Returns the highest and lowest sale."""

sales = [254, 300, 150, 400, 500, 600, 700, 800, 900, 1000]

def sales_sum(sales: list , run = True):
    total_sales = sum(sales)
    if run == True:
        return total_sales
def sales_avg(sales: list, run = True):
    if run == True:
        return sum(sales)/len(sales)
def sales_high_low(sales: list , run = True):
    if run == True:
        return max(sales) , min(sales)
print(sales_sum(sales, True), sales_avg(sales, True), sales_high_low(sales, True))

"""Employee Manager (Dicts + Conditionals)
Create a dictionary with 5 employees and their salaries.
Write a function to:
Find the employee with the highest salary.
Find the employee with the lowest salary.
Given a salary threshold (say 55,000), return a list of employees earning above that amount."""

employees = dict(name = ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],salary = [50000, 60000, 55000, 70000, 45000])
#print(employees)
def emp_high_low(emp : dict ):
    above = []
    for x in range(len(emp['salary'])) :
     if emp['salary'][x] > 55000:
            above.append(emp['name'][x])
            above.append(emp['salary'][x])

     high = max(emp['salary'])
     low = min(emp['salary'])
    return high, low , above
print(emp_high_low(employees))

