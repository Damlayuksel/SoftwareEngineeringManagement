
studentgrades=[["Ellon",80,90,"BA"],["Jack",20,90,"CC"],["John",74,80,"BA"]]

def findgrades(student_name):
    for value in studentgrades:
        if value[0]==student_name:
            print(f"Grades of {value[0]} are Midterm:{value[1]} Final:{value[2]} Transktript:{value[3]}")
            return
    print("Student not in the list")


while True:
    student_name=input("Enter the student name you want to learn : ")

    if student_name == "EOT":
        print("EOP")
        break

    else:
        findgrades(student_name)    