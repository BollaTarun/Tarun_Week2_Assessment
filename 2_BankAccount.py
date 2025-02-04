
class BankAccount:

    def __init__(self,amount):
        self.amount=amount

    def deposit(self):
        while True: 
            deposit_amount=int(input("Enter the Amount you want to deposit :\n"))
            if deposit_amount<10:
                print("Minimum Deposit amount is Rs.10")
            else:
                break
        self.amount+=deposit_amount
        print(f"Rs.{deposit_amount} is successfully deposited to your account!!")

    def withdraw(self):
        while True:
            withdraw_amount=int(input("Enter the Amount you want to Withdraw :\n"))
            if(withdraw_amount<=0):
                print("Enter a VALID AMOUNT!!!")
            elif(withdraw_amount>self.amount):
                print("Your Current Balance is insufficient!!!")
            else:
                break
        self.amount-=withdraw_amount
        print(f"Rs.{withdraw_amount} is successfully withdrawed from your account!!")

    def balance(self):
        print(f"Your Current Balance : {self.amount}")

b=BankAccount(int(input("Enter the Current Balance : ")))
b.deposit()
b.balance()
b.withdraw()
b.balance()

print("NEW ACCOUNT HOLDER :\n")
ba=BankAccount(400)
ba.deposit()
ba.balance()
ba.withdraw()
ba.balance()
        
