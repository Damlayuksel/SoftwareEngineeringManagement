tables = {
    1: ("empty", 0),
    2: ("empty", 0),
    3: ("empty", 0),
    4: ("empty", 0),
    5: ("empty", 0)
}

def assign_table(table_number,customer_name,people_count):
    if table_number not in tables:
        print(f"Masa {table_number} mevcut değil")
        return
    status,_=tables[table_number]

    if status != "empty":
        print(f"Masa {table_number} zaten dolu")
    else:
        tables[table_number]=(customer_name,people_count)
        print(f"Masa {table_number} {customer_name} için ayrıldı")

def release_table(table_number):
    if table_number not in tables:
        print(f"Masa {table_number} mevcut değil")
        return
    status,people_count=tables[table_number]
    if status == "empty":
        print(f"Masa {table_number} zaten boş.")
    else:
        print(f"Masa {table_number} {status} tarafından boşaltıldı ({people_count} kişi).")
        tables[table_number] = ("empty", 0)

def show_table_status():
    print("\n Masa Durumları: ")

    for table_number,(status,people_count) in tables.items():
        if status=="empty":
            print(f"Masa {table_number}: Boş")
        else:
            print(f"Masa {table_number}: {status} ({people_count} kişi)")


assign_table(1,"Ahmet",3)
assign_table(2,"Mehmet",2)

release_table(2)
show_table_status()
