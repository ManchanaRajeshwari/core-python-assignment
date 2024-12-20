def average_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    return average
stds = eval(input("Enter name and marks in their subjects (e.g., {'John': [85, 78, 92], 'Alice': [88, 79, 95]}) : "))
average_marks_dict = {}
for student, marks in stds.items():
    average_marks_dict[student] = round(average_marks(marks), 2)
top_student = max(average_marks_dict, key=average_marks_dict.get)
print("\nAverage Marks:", average_marks_dict)
print(f"Top Performer: \"{top_student}\"")
