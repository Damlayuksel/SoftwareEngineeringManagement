import random

# Hash oluşturma fonksiyonu
def makehash(n):
    hashx = ""
    for index in range(0, n):
        newbyte = random.randint(0, 1)
        hashx = hashx + str(newbyte)
    return hashx  # Döngü sonunda hash'i döndürmeliyiz

# Hash kontrol fonksiyonu
def checkhash(hashy, hashlist):
    notassigned = True
    numberofhashes = len(hashlist)

    for ndx in range(0, numberofhashes):
        if hashy == hashlist[ndx]:  # == kullanmalıyız, atama değil karşılaştırma yapıyoruz
            notassigned = False
            return notassigned  # Hash bulunduğunda, duruma göre sonucu döndürüyoruz
    return notassigned  # Döngü bitince False döndürmeliyiz

# Hash değiştirme fonksiyonu
def changehash(hashz, n):
    location = random.randint(0, n-1)
    character = hashz[location:location+1]

    if character == "0":  # Karakteri değiştirmek için karşılaştırma yapmalıyız
        character = "1"  # Atama işlemi yapmalıyız, karşılaştırma değil
    else:
        character = "0"  # Aynı şekilde burada da

    hashz = hashz[0:location] + character + hashz[location+1:]
    return hashz  # Değişen hash'i döndürüyoruz

# Hash ile mesaj almak fonksiyonu
def getmessagefromhash(hashy, hashdict):
    for message, hash_value in hashdict.items():
        if hash_value == hashy:  # Karşılaştırma yapılmalı
            return message  # Mesaj bulunduğunda geri döndür
    return None  # Hiçbir eşleşme bulunmazsa None döndürüyoruz


number = 8
maxsize = 2**number
hashdict = {}

finished = False

while not finished:
    message = input("Enter the message that you want to hash: ")

    if message == "E0T":
        finished = True
        break
    if len(hashdict) >= maxsize:
        print("You have exceeded the capacity of the hash dictionary.")
        break
    if message in hashdict:
        newhash = hashdict[message]
        print("This message was already hashed before:", newhash)

    else:
        newhash = makehash(number)
        listhash = list(hashdict.values())
        usable = False

        while not usable:
            usable = checkhash(newhash, listhash)
            if usable:
                hashdict[message] = newhash
            else:
                newhash = changehash(newhash, number)

        print("Hash for this message:", newhash)

user_hash = input("Enter the hash that you want to return into message: ")
message_from_hash = getmessagefromhash(user_hash, hashdict)

if message_from_hash:
    print(f"Message for hash {user_hash} is {message_from_hash}")
else:
    print(f"No message found for hash {user_hash}")

print(f"Hash dictionary is: {hashdict}")  
