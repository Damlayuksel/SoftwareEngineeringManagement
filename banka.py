def open_account(accounts):
    name=input("Enter accout holders name: ")
    initial_balance=float(input(f"Enter initial balance for {name} : "))
    accounts[name]=initial_balance
    print(f"Account opened for {name} with initial balance: {initial_balance} TL")

def check_balance(accounts):
    name=input("Enter account holder's name: ")

    if name in accounts:
        print(f"Account balance for{name} is {accounts[name]} tl")

    else:
        print(f"No account found for {name}")


def deposit_money(accounts):
    name=input("Enter the name: ")
    if name in accounts:
        amount=float(input(f"Enter amount for deposit :" ))
        accounts[name]+=amount
        print(f"{amount} Tl deposited into {name} account. New balance: {accounts[name]}")

    else:
        print(f"No account found for {name}")

def withdraw_money(accounts):
    name=input("Enter the name: ")

    if name in accounts:
        amount=float(input(f"Enter amount for withdraw: "))
        if amount<accounts[name]:
            accounts[name]-=amount
            print(f"{amount} tl withdrawn from {name} account. New balance: {accounts[name]}")

        else:
            print(f"Insufficient balance.")
    else:
        print(f"No accound found ")

def main():
    accounts={}

    while True:
        print("\n1. Open Account\n2. Check Balance\n3. Deposit Money\n4. Withdraw Money\n5. Exit")
        choice = input("Choose an option: ")

        if choice=="1":
            open_account(accounts)
        elif choice=="2":
            check_balance(accounts)
        elif choice=="3":
            deposit_money(accounts)
        elif choice=="4":
            withdraw_money(accounts)
        elif choice=="5":
            print("Exiting program")
            break
        else:
            print("Invalid choice")

main()

        

