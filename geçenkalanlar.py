

def generate_pass_fail():

    passed=[]
    failed=[]

    while True:
        name=input("Enter student name= ")
        if name=="EOT":
            break
        grade=int(input(f"Enter grade: "))

        if grade>=50:
            passed.append(name)
        else:
            failed.append(name)
        
    print("PASSED STUDENTS:")

    for students in passed:
        print(students)

    print("FAİLED STUDENTS: ")
    for students in failed:
        print(students)

generate_pass_fail()