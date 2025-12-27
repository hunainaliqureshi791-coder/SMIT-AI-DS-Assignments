attendance = {}

while True:
    name = input("Enter student name (or 'done' to finish): ")
    if name.lower() == "done":
        break

    while True:
        status = input("Enter attendance (P/A): ").upper()
        if status == "P" or status == "A":
            attendance[name] = status
            break
        else:
            print("Invalid input! Please enter P or A.")

present = list(attendance.values()).count("P")
absent = list(attendance.values()).count("A")
total_students = len(attendance)

percentage = (present / total_students) * 100 if total_students > 0 else 0

print("\n----- Attendance Report -----")
print("Total Students:", total_students)
print("Present:", present)
print("Absent:", absent)
print(f"Attendance Percentage: {percentage:.2f}%")
