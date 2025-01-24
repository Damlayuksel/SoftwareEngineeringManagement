from datetime import datetime

trees = {
    "Apple": ["Malus Sylvestris", 4],
    "Avocado": ["Persea Americana", 9],
    "Fig": ["Ficus Carica", 5]
}

towns = {
    "Ankara": 7,
    "Bodrum": 10,
    "Erzurum": 4
}

orders = {}

while True:
    customer_name = input("Customer name: ")
    if customer_name == "EOT":
        break
    town_name = input("Town: ")
    sampling_name = input("Sampling name: ")

    if town_name in towns and sampling_name in trees:
        town_hardiness = towns[town_name]
        sampling_hardiness = trees[sampling_name][1]

        if town_hardiness < sampling_hardiness:
            orders[customer_name] = [town_name, sampling_name, "denied"]
        else:
            current_date = datetime.now().strftime("%Y/%m/%d")
            orders[customer_name] = [town_name, sampling_name, current_date]
    else:
        print("Enter valid value")

print("Final Order:")

for customer, details in orders.items():
    print(f"{customer}: {details}")
