orders = {
    "Müşteri1": [("Pizza", 1, 50), ("Salata", 2, 20)],
    "Müşteri2": [("Kebap", 3, 80)]
}

def add_order(customer_name,product,quantity,price):
    if customer_name not in orders:
        orders[customer_name]=[]
    orders[customer_name].append((product,quantity,price))
    print(f"{customer_name} için {product} siparişi eklendi")

def calculate_total(customer_name):
    if customer_name not in orders:
        print(f"{customer_name} kayıtlarda yok")
        return 0
    
    total=sum(quantity*price for _,quantity,price in orders[customer_name])
    print(f"{customer_name} toplam borcu: {total}")
    return total

def daily_report():
    total_revenue=0
    print("\nGün Sonu Raporu:")
    print("Müşteri Adı | Ürünler | Toplam Borç")
    print("-" * 40)

    for customer_name,customer_orders in orders.items():
        customer_total=calculate_total(customer_name)
        total_revenue+=customer_total
        
        products = ", ".join([f"{product} ({quantity}x)" for product, quantity, _ in customer_orders])
        print(f"{customer_name} | {products} | {customer_total} birim")

    print("-" * 40)
    print(f"Toplam Günlük Gelir: {total_revenue} birim.")

add_order("Müşteri1", "Burger", 2, 30)
add_order("Müşteri3", "Pizza", 1, 50)

calculate_total("Müşteri1")
daily_report()


