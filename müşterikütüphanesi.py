from datetime import datetime

customers = {}


date_format = "%d/%m/%Y"


def add_rental(customer_name, book_name, rental_date):
    rental_date = datetime.strptime(rental_date, date_format)
    if customer_name not in customers:
        customers[customer_name] = [0, []]
    customers[customer_name][1].append((book_name, rental_date, None))
    print(f"{customer_name} adlı müşteri '{book_name}' kitabını {rental_date.strftime(date_format)} tarihinde kiraladı.")


def return_book(customer_name, book_name, return_date):
    return_date = datetime.strptime(return_date, date_format)
    if customer_name in customers:
        for i, (book, rental_date, _) in enumerate(customers[customer_name][1]):
            if book == book_name and _ is None:
                # Gecikme hesaplama
                delay_days = (return_date - rental_date).days - 7
                if delay_days > 0:
                    penalty = delay_days * 10
                    customers[customer_name][0] += penalty
                    print(f"Gecikme cezası: {penalty} birim ({delay_days} gün gecikme)")
                else:
                    print(f"{book_name} kitabı zamanında iade edildi.")
                # İade tarihi güncelle
                customers[customer_name][1][i] = (book, rental_date, return_date)
                return
        print(f"{book_name} kitabı bulunamadı veya zaten iade edilmiş.")
    else:
        print(f"{customer_name} adlı müşteri kayıtlı değil.")

# Gün sonu raporu
def daily_report():
    print("\n--- Gün Sonu Raporu ---")
    total_fines = 0
    delinquent_customers = []
    for customer_name, (debt, rentals) in customers.items():
        print(f"\nMüşteri: {customer_name}")
        print(f"Toplam Borç: {debt} birim")
        for book, rental_date, return_date in rentals:
            rental_info = f"{book} (Kiralanma: {rental_date.strftime(date_format)}"
            rental_info += f", İade: {return_date.strftime(date_format) if return_date else 'Henüz iade edilmedi'})"
            print(f"  - {rental_info}")
        total_fines += debt
        if debt > 0:
            delinquent_customers.append(customer_name)
    
    print("\nGünlük Toplam Cezalar: ", total_fines)
    print("Borçlu Müşteriler: ", delinquent_customers if delinquent_customers else "Yok")
    print("--- Rapor Bitti ---")

# Ana döngü
while True:
    print("\n--- Kütüphane Yönetim Sistemi ---")
    print("1. Yeni kiralama")
    print("2. Kitap iadesi")
    print("3. Gün sonu raporu")
    print("4. Çıkış")
    choice = input("Seçiminizi yapın: ")
    
    if choice == "1":
        customer_name = input("Müşteri adı: ")
        book_name = input("Kitap adı: ")
        rental_date = input("Kiralanma tarihi (dd/mm/yyyy): ")
        add_rental(customer_name, book_name, rental_date)
    elif choice == "2":
        customer_name = input("Müşteri adı: ")
        book_name = input("Kitap adı: ")
        return_date = input("İade tarihi (dd/mm/yyyy): ")
        return_book(customer_name, book_name, return_date)
    elif choice == "3":
        daily_report()
    elif choice == "4":
        print("Sistemden çıkılıyor...")
        break
    else:
        print("Geçersiz seçim! Tekrar deneyin.")
