
print("=" * 55)
print("           PYTHON PROJECT - 13")
print("     STUDENT ATTENDANCE MANAGEMENT SYSTEM")
print("=" * 55)
print("  Project: Student Attendance Management")
print("  Attendance Threshold: 75%")
print("  Language: Python")
print("=" * 55)


FILE_NAME = "attendance.txt"
THRESHOLD = 75


# Clean and format student name
def clean_name(name):
    name = name.strip()
    name = name.title()
    return name


# Count present days
def count_present(marks):
    count = 0

    for mark in marks:
        if mark == "P":
            count = count + 1

    return count


# Count recorded days
def count_recorded(marks):
    count = 0

    for mark in marks:
        if mark == "P" or mark == "A":
            count = count + 1

    return count


# Calculate attendance percentage
def attendance_percentage(marks):
    present = count_present(marks)
    total = count_recorded(marks)

    if total == 0:
        return 0

    percentage = (present / total) * 100
    return percentage


# Load attendance from file
def load_data():
    attendance = {}

    try:
        file = open(FILE_NAME, "r")

        for line in file:
            line = line.strip()

            if "|" in line:
                parts = line.split("|")

                name = clean_name(parts[0])
                marks = parts[1].split(",")

                if name:
                    attendance[name] = marks

        file.close()

    except FileNotFoundError:
        print("No saved file found. Starting with empty data.")

    return attendance


# Save attendance to file
def save_data(attendance):
    try:
        file = open(FILE_NAME, "w")

        for name in sorted(attendance):
            marks = attendance[name]

            data = ",".join(marks)

            file.write(name + "|" + data + "\n")

        file.close()

        print("Attendance saved successfully.")

    except OSError:
        print("Unable to save attendance.")


# Add a new student
def add_student(attendance):
    name = input("Enter student name: ")
    name = clean_name(name)

    if name == "":
        print("Name cannot be empty.")

    elif "|" in name or "," in name:
        print("Name cannot contain | or , characters.")

    elif name in attendance:
        print("Student already exists.")

    else:
        total_days = 0

        for marks in attendance.values():
            if len(marks) > total_days:
                total_days = len(marks)

        attendance[name] = []

        for i in range(total_days):
            attendance[name].append("-")

        print(name, "added successfully.")


# Mark attendance
def mark_attendance(attendance):
    if len(attendance) == 0:
        print("Please add students first.")
        return

    total_days = 0

    for marks in attendance.values():
        if len(marks) > total_days:
            total_days = len(marks)

    day = total_days + 1

    for name in sorted(attendance):
        while True:
            mark = input(name + " (P/A): ")
            mark = mark.upper().strip()

            if mark == "P" or mark == "A":
                attendance[name].append(mark)
                break

            else:
                print("Enter only P or A.")

    print("Attendance marked for Day", day)


# Display attendance register
def show_register(attendance):
    if len(attendance) == 0:
        print("No student records available.")
        return

    total_days = 0

    for marks in attendance.values():
        if len(marks) > total_days:
            total_days = len(marks)

    print()
    print("Student".ljust(22), end="")

    for day in range(1, total_days + 1):
        print(("D" + str(day)).rjust(5), end="")

    print()

    for name in sorted(attendance):
        print(name.ljust(22), end="")

        marks = attendance[name]

        for day in range(total_days):
            if day < len(marks):
                print(marks[day].rjust(5), end="")
            else:
                print("-".rjust(5), end="")

        print()


# Show attendance percentages
def show_percentages(attendance):
    if len(attendance) == 0:
        print("No student records available.")
        return

    for name in sorted(attendance):
        marks = attendance[name]

        present = count_present(marks)
        total = count_recorded(marks)

        percentage = attendance_percentage(marks)

        print(name, ":", round(percentage, 2), "%")

        print("Present:", present, "/", total)


# Show students below 75 percent
def show_shortage(attendance):
    found = False

    for name in sorted(attendance):
        marks = attendance[name]

        total = count_recorded(marks)

        if total > 0:
            percentage = attendance_percentage(marks)

            if percentage < THRESHOLD:
                print(name, ":", round(percentage, 2), "%")
                found = True

    if found == False:
        print("No students have attendance below 75%.")


# Show absent students for a particular day
def show_absentees(attendance):
    if len(attendance) == 0:
        print("No student records available.")
        return

    day = input("Enter day number: ")

    if day.isdigit() == False or int(day) <= 0:
        print("Enter a valid day number.")
        return

    day = int(day)

    absentees = set()

    for name in attendance:
        marks = attendance[name]

        if len(marks) >= day:
            if marks[day - 1] == "A":
                absentees.add(name)

    if len(absentees) > 0:
        print("Absent students on Day", day)

        for name in sorted(absentees):
            print(name)

    else:
        print("No absentees recorded for that day.")


# Show all registered students
def show_students(attendance):
    if len(attendance) == 0:
        print("No students registered.")
        return

    print("\nRegistered Students:")

    for name in sorted(attendance):
        print(name)


# Main menu
def main():
    attendance = load_data()

    while True:
        print("\n========== ATTENDANCE MANAGEMENT ==========")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance Register")
        print("4. Show Attendance Percentages")
        print("5. Show Students Below 75%")
        print("6. Show Absentees for a Day")
        print("7. View All Students")
        print("8. Save Attendance")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student(attendance)

        elif choice == "2":
            mark_attendance(attendance)

        elif choice == "3":
            show_register(attendance)

        elif choice == "4":
            show_percentages(attendance)

        elif choice == "5":
            show_shortage(attendance)

        elif choice == "6":
            show_absentees(attendance)

        elif choice == "7":
            show_students(attendance)

        elif choice == "8":
            save_data(attendance)

        elif choice == "9":
            save_data(attendance)
            print("Thank you for using Attendance Management System.")
            break

        else:
            print("Invalid choice. Please enter 1 to 9.")


main()
