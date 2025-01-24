hashdict={ 'how are you': '010100'
           ,  'hello': '110100',
            'goodmornin': '000100' }

finished=False

while not finished:
    user_input=input("Enter a message or hash to search it = ")

    if user_input=="EOT":
        print("EOP")
        finished=True

    else:
        if user_input in hashdict:
            print(f"Hash for {user_input} is {hashdict[user_input]}")

        elif user_input in hashdict.values():
            message=[key for key,value in hashdict.items() if value==user_input] [0]
            print(f"Message for hash {user_input} is {message}")

        else:
            print(f"{user_input} is not in the list")

