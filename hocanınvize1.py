def calculate_payment():
    while True:
        name = input("Çalışanın adını girin (veya 'END' yazarak çıkış yapın): ")
        if name == "END":
            print("Program sonlandırıldı.")
            break

        try:
            net_hourly_wage = float(input(f"{name} için net saatlik ücreti girin: "))
            hours_worked = float(input(f"{name} için haftalık çalışma saatini girin: "))

            
            if net_hourly_wage * hours_worked < 992:
                print("Net haftalık maaş 992 TL'den az olamaz. Lütfen veriyi düzeltin.")
                continue

            if hours_worked > 45:
                print("Haftalık çalışma süresi 45 saatten fazla olamaz. Lütfen veriyi düzeltin.")
                continue

            if hours_worked > 40:
                overtime_hours = hours_worked - 40
                overtime_rate = net_hourly_wage * 1.5
                payment = (40 * net_hourly_wage) + (overtime_hours * overtime_rate)
            else:
                payment = hours_worked * net_hourly_wage

            print(f"{name} için hesaplanan ödeme: {payment:.2f} TL")
        
        except ValueError:
            print("Geçerli bir sayı girmelisiniz. Lütfen tekrar deneyin.")


calculate_payment()
