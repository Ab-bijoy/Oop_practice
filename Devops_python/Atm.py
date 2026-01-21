class Atm:
    def __init__(self):
        self.__balance=0
        self.__pin =""
        self.menu()
    
    def menu(self):
        user_input = input( """

        Hello, how may I help you?
        1. Create Pin
        2. Check Balance
        3. Deposit
        4. Withdraw
        5. Exit
        
        """)

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.check_balance()
        elif user_input == "3":
            self.deposit()
        elif user_input == "4":
            self.withdraw()
        elif user_input == "5":
            self.exit()
        
    def create_pin(self):
        self.__pin=input("Enter your pin: ")
        print("Pin created successfully")
    def deposit(self):
        temp = input("Enter your pin: ")
        if temp ==self.__pin:
            amount = int(input("Enter the amount: "))
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid pin")
    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp ==self.__pin:
            print("Your balance is: ",self.__balance)
        else:
            print("Invalid pin")
    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp ==self.__pin:
            amount = int(input("Enter the amount: "))
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal successful")
            else:
                print("Insufficient balance")
        else:
            print("Invalid pin")
    def exit(self):
        print("Thank you for using our services")


