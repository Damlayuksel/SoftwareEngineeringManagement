import time

# Geçerli zaman
var = time.localtime()

# Ayları sayılara dönüştürmek için fonksiyon
def getmonth(month):
    if month == "Jan":
        return "01"
    elif month == "Feb":
        return "02"
    elif month == "Mar":
        return "03"
    elif month == "Apr":
        return "04"
    elif month == "May":
        return "05"
    elif month == "Jun":
        return "06"
    elif month == "Jul":
        return "07"
    elif month == "Aug":
        return "08"
    elif month == "Sep":
        return "09"
    elif month == "Oct":
        return "10"
    elif month == "Nov":
        return "11"
    elif month == "Dec":
        return "12"
    else:
        return "Invalid month"


# Tarih bilgisini alıp doğru formatta döndüren fonksiyon
def getdate(chrstr):
    day = chrstr[8:10]
    mnt = chrstr[4:7]
    month = getmonth(mnt)
    year = chrstr[20:24]  # Yılı doğru şekilde alıyoruz
    result = day + "/" + month + "/" + year  # Yeni satır karakteri yerine tarih formatı
    return result


# Öğrenciler için başlangıç verileri
grades = [["Ali", 75, "10/09/2024"], ["Damla", 95, "10/09/2024"], ["Pemıla", 35, "10/09/2024"]]

bitti = False

# Kullanıcıdan yeni öğrenciler ve notlar almak
while not bitti:
    name = input("Enter the name of student: ")
    midterm = input("Enter midterm grade: ")

    # Tarih bilgisini almak
    datentime = time.strftime("%c", var)
    dateinfo = getdate(datentime)

    # Öğrencinin bilgilerini listeye eklemek
    innerlist = [name, float(midterm), dateinfo]
    grades.append(innerlist)

    # Başka öğrenci eklemek isteyip istemediğini soralım
    continue_input = input("Do you want to add another student? (y/n): ")
    if continue_input.lower() != 'y':
        bitti = True

# Sonuçları ekrana yazdırma
for student in grades:
    print(student)
