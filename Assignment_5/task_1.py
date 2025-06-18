# create a dictionary of student marks
student_marks = {
    "Alice": 85,
    "Adesh": 90,
    "Yogesh": 78,
    "Rohit": 92,
}

student_name = input("Enter the student's name: ").strip()
if student_marks.get(student_name) is not None:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found.")