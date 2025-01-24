players = {
    "Messi": ["Lionel", "PSG"],
    "Ronaldo": ["Cristiano", "ManUnited"],
    "Lewandowski": ["Robert", "Barcelona"],
    "Valencia": ["Enner", "Fenerbahce"],
    "Haaland": ["Erling", "ManCity"],
    "Tatum": ["Jayson", "Celtics"],
    "Salah": ["Mohammed", "Liverpool"],
    "Curry": ["Steph", "Warriors"],
    "Mbappe": ["Kylian", "PSG"],
    "James": ["LeBron", "Lakers"],
    "Ghezzal": ["Rachid", "Besiktas"],
    "Muslera": ["Fernando", "Galatasaray"]
}


while True:
    print("Eklemek istediğiniz oyuncu bilgilerini girin:")
    last_name=input("Last name:")
    
    if last_name=="EOT":
        break
    first_name=input("Name:")
    club=input("Club:")

    players[last_name]=[first_name,club]

sorted_players=dict(sorted(players.items()))

print("Sıralanmış oyuncu listesi:")

for last_name,details in sorted_players.items():
    print(f"Soyad: {last_name}, Ad:{details[0]}, Kulüp{details[1]}")