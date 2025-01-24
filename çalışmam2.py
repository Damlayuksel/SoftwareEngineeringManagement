

grades= [["Ela",50,70,"C"],["Donald",60,50,"D"],["Kemal",50,80,"C"]]


def get_grades():
    while True:
        name=input("Enter the student name= ")

        found=False
        for student in grades:
            if student[0]==name:
                print(f"Grades: {student[1]} , {student[2]}, {student[3]}")
                found=True
                break

        if not found:
            print("Student not found in the list try it again")


get_grades()