# OS Bank
Person = []

class Account:
    Title = "\n*** Hello in bank HTM ***\n"
    print(Title)

    def __init__(self):
        while True:
            print("\n1- Create Account Bank")
            print("2- Show Accounts")
            print("3- Remove Account")
            print("4- Deposit and Withdraw money")
            print("5- Exit")

            try:
                self.x = int(input("Choose number: "))
            except ValueError:
                print("⚠️ Please enter a valid number.")
                continue

            if self.x == 5:
                print("### Good luck at work ###")
                break
            elif self.x == 1:
                self.create_account()
            elif self.x == 2:
                self.show_accounts()
            elif self.x == 3:
                self.remove_account()
            elif self.x == 4:
                self.deposit_withdraw()
            else:
                print("⚠️ Invalid choice, try again.")

    def create_account(self):
        while True:
            acc_type = input("Current or Saving ? ").strip().lower()
            if acc_type == "current":
                full_name = input("Full Name: ")
                cni = input("Carte National Identification N*: ")
                try:
                    phone = int(input("Number Phone: "))
                    balance = float(input("Balance: "))
                except ValueError:
                    print("⚠️ Phone and Balance must be numbers.")
                    continue
                email = input("Email: ")
                city = input("City: ")
                Person.append([full_name, cni, phone, email, city, balance])
                print("\n✅ Done, welcome in bank HTM\n")
                break
            elif acc_type == "saving":
                print("\n### we don't work that way, SORRY!! ###\n")
                break
            else:
                print("⚠️ Error: please type 'Current' or 'Saving'.")

    def show_accounts(self):
        if not Person:
            print("No accounts found.")
        else:
            for i, data in enumerate(Person, 1):
                print(f"{i}- {data}")

    def remove_account(self):
        if not Person:
            print("No accounts to remove.")
            return
        self.show_accounts()
        while True:
            try:
                number = int(input("Choose number to remove: "))
                if 1 <= number <= len(Person):
                    Person.pop(number - 1)
                    print("✅ Removed Successfully")
                    break
                else:
                    print("⚠️ Number out of range.")
            except ValueError:
                print("⚠️ Please enter a valid number.")

    def deposit_withdraw(self):
        if not Person:
            print("No accounts available for deposit or withdrawal.")
            return

        t = input("Do you want to deposit or withdraw? ").strip().lower()
    
        if t not in ["deposit", "withdraw"]:
            print("Please choose either 'deposit' or 'withdraw'.")
            return

        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                return
        except ValueError:
            print("Please enter a valid number!")
            return

        for index in Person:
            if t == "deposit":
                index[5] += amount
                print(f"Deposit successful! Current balance: {index[5]}")
            elif t == "withdraw":
                if amount > index[5]:
                    print(f"Insufficient funds! Current balance: {index[5]}")
                else:
                    index[5] -= amount
                    print(f"Withdrawal successful! Current balance: {index[5]}")

Account()
