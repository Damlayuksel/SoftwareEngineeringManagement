# Kullanıcıdan bir sayı al
sayi = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin: "))

# Faktöriyel hesaplama
faktoriyel = 1
if sayi < 0:
    print("Negatif sayıların faktöriyeli hesaplanamaz.")
elif sayi == 0:
    print("0! = 1")
else:
    for i in range(1, sayi + 1):
        faktoriyel *= i
    print(f"{sayi}! = {faktoriyel}")



##### FIBONACCI
# Kullanıcıdan bir sayı al
n = int(input("Kaç terimlik Fibonacci serisi istiyorsunuz? "))

# İlk iki terim
a, b = 0, 1
count = 0
if n <= 0:
    print("Lütfen pozitif bir sayı girin.")
elif n == 1:
    print(f"Fibonacci serisi: {a}")
else:
    print("Fibonacci serisi:")
    while count < n:
        print(a, end=", ")
        toplam = a + b
        a = b
        b = toplam
        count += 1

######### ASAL SAYI

# Kullanıcıdan bir sayı al
sayi = int(input("Bir sayı girin: "))

# Asal sayı kontrolü
if sayi > 1:
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            print(f"{sayi} bir asal sayı değildir.")
            break
    else:
        print(f"{sayi} bir asal sayıdır.")
else:
    print(f"{sayi} bir asal sayı değildir.")

########## POZİTİF NEGATİF

# Kullanıcıdan bir sayı al
sayi = float(input("Bir sayı girin: "))

# Pozitif, negatif ya da sıfır durumlarını kontrol et
if sayi > 0:
    print("Sayı pozitiftir.")
elif sayi < 0:
    print("Sayı negatiftir.")
else:
    print("Sayı sıfırdır.")



sayi = int(input("Bir sayı girin: "))

# Sayının tek mi çift mi olduğunu kontrol et
if sayi % 2 == 0:
    print("Sayı çifttir.")
else:
    print("Sayı tektir.")





