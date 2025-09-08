print("This is Day 2")

"""
Create dataset
Each student should be a dictionary with keys:
"name" (string) , "marks" (integer, 0–100), "grade" (string, A/B/C based on marks)
1. Highest Marks Function: Write a function top_student(students) → returns the dictionary of the student with the highest marks.
2. Grade Count Function: Write a function count_grade(students, grade) → returns how many students got that grade (e.g., "A").
3. Average Marks Function: Write a function average_marks(students) → returns the average of all students’ marks.
4. Bonus (Optional): Sort the list of students by marks (highest → lowest) and print their names in order.
"""

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

def top_student (students: list):
    top = max(students, key = lambda x: x['marks'])
    return top
print(top_student(students))
def count_grade(students, grade: str):
    count = 0
    for i in students:
        if i["grade"] == grade:

            count += 1
    return count
print(count_grade(students, "A"))

print(len(students))

def avg_student (students: list):
    avg_stu = []
    for i in students :
        avg = sum(i["marks"] for i in students) / len(students)
        if i["marks"] > avg :
            avg_stu.append(i["name"])
    return avg_stu , avg
print(avg_student(students))

def sort_students(students: list):

    sorted_studs = sorted(students , key  = lambda x: x["marks"] , reverse = True)
    names = [students['name'] for students in sorted_studs]
    return names
print(sort_students(students))