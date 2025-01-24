
students = [
    ["Alice", 50, 70, "C"],
    ["Bob", 60, 50, "D"],
    ["Charlie", 50, 80, "C"]
]

# Öğrenci notlarını bulan fonksiyon
def find_grades(student_name):
    for value in students:
        if value[0] == student_name: 
            print(f"Grades of {value[0]} - Midterm: {value[1]}, Final: {value[2]}, Transcript: {value[3]}")
            return
    print("Student not in the list")

# Kullanıcıdan giriş alma döngüsü
while True:
    student_name = input("Enter the student you want to learn grade (or type 'EOT' to exit): ")

    if student_name == "EOT":
        print("End of Program")
        break
    else:
        find_grades(student_name)  
