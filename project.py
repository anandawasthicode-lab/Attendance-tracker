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