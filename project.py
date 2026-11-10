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