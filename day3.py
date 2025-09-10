print("This is Day 3")


"""Custom Min/Max/Average (Lists)

Create a list of 15 random integers (1–100).
Write your own functions (don’t use min(), max(), or sum()):
my_min(lst) → returns smallest number.
my_max(lst) → returns largest number.
my_avg(lst) → returns average. """

list_of_int = [34, 67, 23, 89, 12, 90, 45, 78, 56, 11, 99, 43, 21, 5, 88]

def my_min(lst: list):
    min = lst[0]
    for i in lst :
        if i < min:
            min = i
    return min
print(my_min(list_of_int))

def my_max(lst: list):
    min = lst[0]
    for i in lst :
        if i > min:
            min = i
    return min
print(my_max(list_of_int))

def my_avg(lst: list):
    avg = sum (lst)/len(lst)
    return avg
print(my_avg(list_of_int))


"""Create a dictionary of monthly sales:
Write a loop to:
Find the month with the highest sales.
Find the month with the lowest sales.
Calculate the total sales for first 3 months."""

monthly_sales = { "Jan": 1200, "Feb": 1500, "Mar": 1700, "Apr": 1600, "May": 1800, "Jun": 2000, "Jul": 2200, "Aug": 2100, "Sep": 1900, "Oct": 2300, "Nov": 2500, "Dec": 2400}
def sales_data(sales: dict):
    sales_lst = list(sales.items())
    total_sales = 0
    first_month , first_sale = sales_lst[0]
    min_month , min_sales = first_month , first_sale
    max_month , max_sales = first_month , first_sale
    for x , y in sales_lst:

        if y > max_sales:
            max_sales = y
            max_month = x
            sales = y
        elif y < min_sales:
            min_sales = y
            min_month = x
    for x , y in sales_lst[:3]:
        total_sales += y

    return max_month , max_sales , min_month , min_sales , total_sales
print(sales_data(monthly_sales))


"""Student Pass/Fail (Conditionals)
Reuse your students list from Day 2.
Write a function pass_fail(students, cutoff) that:
Returns 2 lists → one with names of students who passed (≥ cutoff), and one with those who failed."""

students = [
    {"name": "Alice", "marks": 85, "grade": "A"},
    {"name": "Bob", "marks": 72, "grade": "B"},
    {"name": "Charlie", "marks": 91, "grade": "A"},
    {"name": "David", "marks": 65, "grade": "C"},
    {"name": "Evelyn", "marks": 78, "grade": "B"},
    {"name": "Frank", "marks": 55, "grade": "D"},
    {"name": "Grace", "marks": 88, "grade": "A"},
    {"name": "Hannah", "marks": 60, "grade": "C"},
]



def  pass_fail(students: list , cutoff):
    passed  = []
    failed = []
    for i in students:
        if i["marks"] >= cutoff :
            passed.append(i["name"])
        else:
            failed.append(i["name"])
    return passed , failed
print(pass_fail(students, 85))