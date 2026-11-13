print("=" * 55)
print("           PYTHON PROJECT - 13")
print("  STUDENT ATTENDANCE MANAGEMENT SYSTEM")
print("=" * 55)
print("  Project: Student Attendance Management")
print("  Attendance Threshold: 75%")
print("  Language: Python")
print("=" * 55)
print()

import doctest

FILE_NAME = "attendance.txt"
THRESHOLD = 75.0


# Clean and validate a student's name.
def clean_name(name):
    """
    >>> clean_name("  anand awasthi  ")
    'Anand Awasthi'
    """
    return " ".join(name.strip().split()).title()
# Count present days using recursion.
def count_present(marks):
    """
    >>> count_present(["P", "A", "P", "P"])
    3
    """
    if len(marks) == 0:
        return 0
    if marks[0] == "P":
        return 1 + count_present(marks[1:])
    return count_present(marks[1:])
# Calculate attendance percentage.
def attendance_percentage(marks):
    """
    >>> attendance_percentage(["P", "A", "P"])
    66.66666666666666
    """
    recorded_days = sum(1 for mark in marks if mark in ("P", "A"))

    if recorded_days == 0:
        return 0.0

    return count_present(marks) / recorded_days * 100
#Load attendance data from a text file.
def load_data():
    attendance = {}
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()
                if not line or "|" not in line:
                    continue

                name, data = line.split("|", 1)
                name = clean_name(name)
                marks = data.split(",") if data else []

                if name and all(mark in ("P", "A", "-") for mark in marks):
                    attendance[name] = marks

    except FileNotFoundError:
        print("No saved file found. Starting with empty data.")
    except (OSError, UnicodeError) as error:
        print("Could not read the attendance file:", error)

    return attendance

# Save all attendance records to a text file.
def save_data(attendance):
    try:
        with open(FILE_NAME, "w") as file:
            for name in sorted(attendance):
                file.write(name + "|" + ",".join(attendance[name]) + "\n")
        print("Attendance saved successfully.")
        return True
    except (OSError, UnicodeError) as error:
        print("Could not save attendance:", error)
        return False

# Read a non-empty value from the user.
def get_text(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


# Read a positive day number.
def get_day_number():
    while True:
        value = input("Enter day number: ").strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Enter a valid positive day number.")


# Add a new student.
def add_student(attendance):
    name = clean_name(get_text("Enter student name: "))

    if "|" in name or "," in name or "\n" in name:
        print("Name cannot contain | or , characters.")
    elif name in attendance:
        print("Student already exists.")
    else:
        total_days = max(
            (len(marks) for marks in attendance.values()),
            default=0
        )
        attendance[name] = ["-"] * total_days
        print(name, "added successfully.")