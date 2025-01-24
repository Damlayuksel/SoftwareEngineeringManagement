from datetime import datetime

borrowed_books = []

def borrow_book():
    book_name = input("Kitap adı: ")
    borrow_date_str = input("Ödünç alınma tarihi (gg/aa/yyyy): ")
    borrow_date = datetime.strptime(borrow_date_str, "%d/%m/%Y")
    borrowed_books.append({"name": book_name, "borrow_date": borrow_date, "return_date": None})
    print(f"'{book_name}' kitabı ödünç alındı.")

def return_book():
    book_name = input("İade edilen kitabın adı: ")
    return_date_str = input("İade tarihi (gg/aa/yyyy): ")
    return_date = datetime.strptime(return_date_str, "%d/%m/%Y")
    
    for book in borrowed_books:
        if book["name"] == book_name and book["return_date"] is None:
            book["return_date"] = return_date
            delay_days = (return_date - book["borrow_date"]).days - 7
            if delay_days > 0:
                penalty = delay_days * 5
                print(f"{delay_days} gün gecikme için {penalty} TL ceza.")
            else:
                print(f"'{book_name}' kitabı zamanında iade edildi.")
            return
    
    print(f"'{book_name}' kitabı bulunamadı veya zaten iade edilmiş.")

def daily_report():
    print("\nGünlük Rapor:")
    total_penalty = 0
    for book in borrowed_books:
        status = "İade Edilmedi" if book["return_date"] is None else f"İade Tarihi: {book['return_date'].strftime('%d/%m/%Y')}"
        print(f"Kitap: {book['name']}, Ödünç Alınma: {book['borrow_date'].strftime('%d/%m/%Y')}, Durum: {status}")
        if book["return_date"]:
            delay_days = (book["return_date"] - book["borrow_date"]).days - 7
            if delay_days > 0:
                total_penalty += delay_days * 5
    print(f"Toplam Ceza: {total_penalty} TL\n")

def main():
    while True:
        print("\nKütüphane Yönetim Sistemi")
        print("1. Kitap ödünç al")
        print("2. Kitap iade et")
        print("3. Günlük rapor")
        print("4. Çıkış")
        choice = input("Seçim: ")
        
        if choice == "1":
            borrow_book()
        elif choice == "2":
            return_book()
        elif choice == "3":
            daily_report()
        elif choice == "4":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim!")

main()
