
müşteriler={}

def müşteri_ekle(müşteriler):
    isim=input("Müşteri adı:")
    telefon=input("Telefon numarası:")
    borç=float(input("Borç miktarı:"))
    müşteriler[isim]={"telefon":telefon,"Borç":borç}
    print(f"{isim} eklendi")


def borç_güncelle(müşteriler):
    isim=input("Borcunu güncellemek istediğiniz müşterinin adı: ")
    if isim in müşteriler:
        değişim=float(input("Borç değişim miktarı: "))
        müşteriler[isim]["Borç"]+=değişim
    else:
        print(f"{isim} sistemde bulunamadı")

def müşteri_sil(müşteriler):
    isim=input("Silmek istediğiniz müşteri adını girin: ")
    if isim in müşteriler:
        müşteriler.pop(isim)
        print(f"{isim} Başarıyla silindi")

    else:
        print(f"{isim} sistemde bulunamadı")

def müşteri_bilgileri(müşteriler):
    for isim,bilgiler in müşteriler.items():
        print(f"Müşteri Adı: {isim}")
        print(f"Telefon Numarası: {bilgiler['telefon']}")
        print(f"Borç Miktarı: {bilgiler['Borç']:.2f} TL")
        print("****************************")

def toplam_borç(müşteriler):
    toplam_borç=sum(bilgiler["Borç"] for bilgiler in müşteriler.values())
    print(f"Sistemdeki müşterilerin toplam borcu: {toplam_borç:.2f} TL")

def borçsuz_müşteriler(müşteriler):
    borçsuzlar=[isim for isim,bilgiler in müşteriler.items() if bilgiler["Borç"] ==0]
    if borçsuzlar:
        print("\nBorcu olmayan müşteriler:")
        for isim in borçsuzlar:
            print(f"- {isim}")
    else:
        print("Borcu olmayan müşteri bulunmamaktadır.")

def borç_ödeme(müşteriler):
    isim=input("Borcunu ödemek istediğiniz müşterinin adı: ")

    if isim in müşteriler:
        ödeme_miktari=float(input("Ödeme miktarı: "))
        if ödeme_miktari>müşteriler[isim]["Borç"]:
            print("Hata: ödeme miktarı borçtan fazla olamaz")
        else:
            müşteriler[isim]["Borç"]-=ödeme_miktari
            print(f"{isim} adlı müşterinin borcu güncellendi. Kalan borç: {müşteriler[isim]['Borç']}")


    else:
        print(f"{isim} sistemde kayıtlı değil")

def enyüksek_borçlu(müşteriler):
    if müşteriler:
        en_yüksek_borçlu=max(müşteriler.items(),key=lambda item: item[1]["Borç"])
        isim,bilgiler=en_yüksek_borçlu
        print(f"\nEn çok borcu olan müşteri: {isim}")
        print(f"Telefon Numarası: {bilgiler['telefon']}")
        print(f"Borç Miktarı: {bilgiler['Borç']:.2f} TL")
    else:
        print("Sistemde müşteri kaydı yok.")

def main():

    while True:


        print("\nMenü:")
        print("1 - Müşteri Ekle")
        print("2 - Borç Güncelle")
        print("3 - Müşteri Sil")
        print("4 - Müşteri Bilgileri")
        print("5 - Toplam Borç")
        print("6 - Borçsuz Müşteriler")
        print("7 - Borç ödeme")
        print("8 - En Yüksek Borç")
        print("9 - Çıkış")

        print("****************************")
            
        choice=input("İşlem seçin ")
        print("****************************")

        if choice=="1":
            müşteri_ekle(müşteriler)
            
        elif choice=="2":
            borç_güncelle(müşteriler)

        elif choice=="3":
            müşteri_sil(müşteriler)
        
        elif choice=="4":
            müşteri_bilgileri(müşteriler)

        elif choice=="5":
            toplam_borç(müşteriler)

        elif choice=="6":
            borçsuz_müşteriler(müşteriler)

        elif choice=="7":
            borç_ödeme(müşteriler)

        elif choice=="8":
            enyüksek_borçlu(müşteriler)

        elif choice=="9":
            print("Çıkış..")
            break

main()