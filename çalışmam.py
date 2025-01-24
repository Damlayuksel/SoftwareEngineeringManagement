
def students():
    student_list = {}

    while True:
        name = input("Enter the name (or type 'exit' to stop): ")
        if name.lower() == 'exit':
            break  # Kullanıcı 'exit' yazarsa döngü sonlanır
        
        try:
            midterm = int(input("Enter the midterm grade: "))
            final = int(input("Enter the final grade: "))
        except ValueError:
            print("Invalid input! Please enter numerical values for grades.")
            continue  # Geçersiz not girişini atlattırır ve tekrar kullanıcıdan bilgi alır

        if name not in student_list:
            student_list[name] = []  # Öğrenci adı daha önce eklenmemişse yeni bir liste oluştur

        student_list[name].append((midterm, final))  # Notları listeye ekle

    # Sonuçları yazdırma
    print("\nStudent Grades:")
    for student, grades in student_list.items():
        print(f"{student}: grades: {grades}")

students()
