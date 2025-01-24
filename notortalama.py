def calculate_average():
    students = []

    while True:
        name = input("Enter student name (or 'EOT' to stop): ")
        if name == "EOT":
            break

        try:
            midterm = int(input(f"Enter midterm grade for {name}: "))
            final = int(input(f"Enter final grade for {name}: "))
        except ValueError:
            print("Please enter numeric values for grades.")
            continue

        average = (midterm * 0.4) + (final * 0.6)
        students.append({"Name": name, "Midterm": midterm, "Final": final, "Average": average})

    print("\nStudents' Grades:")
    for student in students:
        print(f"{student['Name']}: Average = {student['Average']}")

    print("\nFailed Students :")
    for student in students:
        if student['Average'] < 50:
            print(f"{student['Name']} - Average: {student['Average']}")

calculate_average()
