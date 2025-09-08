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

"""String Processing (Loops + Conditionals)
Write a function that:
Takes a sentence as input (e.g., "Python is amazing and fun").
Counts how many words have more than 4 letters.
Reverses the entire sentence (word order stays the same, just characters reverse)."""


def string_processing(sent : str):
    count = 0
    words = sent.split()
    for i in words:
        if len(i) > 4 :
            count += 1
    rev = words[::-1]
    return  count, rev

sent =input("enter a sentence")

count , rev   = string_processing(sent)
print (rev , count)



"""Mini Data File (File Handling Preview)
Create a text file sales.txt with 5 numbers (each on a new line).
Write Python code to:
Read all numbers into a list.
Compute their total and average."""
def file_handling(path: str):
    integer = []
    with open(path,  'r') as f:
        num = f.readlines()
        for i in num:
            integer.append(int(i))
    return integer
path = r"sales.txt"
print(file_handling(path), sum(file_handling(path)), sum(file_handling(path))/len(file_handling(path)))



