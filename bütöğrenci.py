def student_grades():
    makeup_list = {}  # Sözlük
    passed_students = {}  # Sözlük

    while True:
        student_name = input("Enter the student name (or type 'EOT' to end): ")
        if student_name == "EOT":
            break

       
        midterm_grade = int(input("Midterm Grade: "))
        final_grade = int(input("Final Grade: "))
       

        if final_grade < 40:
            makeup_list[student_name] = {"Midterm": midterm_grade, "Final": final_grade}
        else:
            passed_students[student_name] = {"Midterm": midterm_grade, "Final": final_grade}

    print("\nMakeup List:")
    for name, grades in makeup_list.items():
        print(f"{name}: {grades}")

    print("\nPassed Students:")
    for name, grades in passed_students.items():
        print(f"{name}: {grades}")

# Fonksiyonu çalıştır
student_grades()
