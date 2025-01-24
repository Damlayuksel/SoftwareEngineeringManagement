from datetime import datetime

# Müşteri veritabanı
customers = {
    "Allen Mask": [
        [840, 800, "07/08/2024-17:44"], 
        [970, 1000, "08/11/2024-19:03"]
    ],
    "Slim Shady": [
        [720, 720, "24/12/2024-18:787"]
    ],
    "Amber Hurt": [
        [690, 600, "23/04/2023-09:10"], 
        [1071, 1100, "26/08/2024-21:09"], 
        [1517, 1600, "10/01/2025-16:00"]
    ],
}

# Yeni işlemleri test etmek için verilen veri
new_transactions = [
    ("Dr. Indy Jones", 789, 800),
    ("Grimes Swift", 450, 200),
    ("Xaea-Xii Mask", 220, 200),
    ("Amber Hurt", 840, 900),
    ("Allen Mask", 840, 900),
]

def get_current_time():
    return datetime.now().strftime("%d/%m/%Y-%H:%M")

def add_transaction(customer_name, new_sale, new_payment):
    current_time = get_current_time()

    if customer_name not in customers:
        customers[customer_name] = []
    customers[customer_name].append([new_sale, new_payment, current_time])

def generate_report():
    total_sales = 0
    total_payments = 0
    debtors = []

    print("----GÜN SONU RAPORU-----")

    for customer, transactions in customers.items():
        total_customer_sales = sum(t[0] for t in transactions)
        total_customer_payments = sum(t[1] for t in transactions)
        total_payments += total_customer_payments
        total_sales += total_customer_sales

        if total_customer_sales > total_customer_payments:
            debtors.append((customer, total_customer_sales - total_customer_payments))

        print(f"{customer} satış toplamı = {total_customer_sales}")

    print(f"günlük toplam satış: {total_sales} ")
    print(f"Günlük toplam ödeme: {total_payments}")

    print("Borçlu müşteriler: ")
    for debtor, dept in debtors:
        print(f"{debtor}: Borç= {dept}")

def main():
    # Test verilerini işle
    for transaction in new_transactions:
        add_transaction(*transaction)
    
    # Kullanıcıdan giriş almak
    while True:
        customer_name = input("Müşteri ismi girin (Gün sonu için 'ZZZZ' yazın): ")

        if customer_name == "ZZZZ":
            generate_report()
            break

        new_sale = int(input("Yeni satış tutarını girin: "))
        new_payment = int(input("Yeni ödeme tutarını girin: "))
        add_transaction(customer_name, new_sale, new_payment)

# Ana fonksiyonu çalıştır
main()
