# class BankAccount:
#     def __init__(self,name:str,balance:int):
#         self.name=name
#         self.balance=balance
#     def deposit(self):
#             add=int(input("apecify the amount of money to deposit: "))
#             self.balance+=add
#     def withdraw(self):
#             decrease=int(input("apecify the amount of money to withdraw: "))
#             if self.balance>=decrease:
#                 self.balance-=decrease
#             else :
#                  print("not enough balance")
#     def show_balance(self):
#         print(f" {self.name} balance : {self.balance}")



class BankAccount:
    def __init__(self,name:str,balance:int):
        self.name=name
        self.balance=balance
    def deposit(self,add:int):
            self.balance+=add
    def withdraw(self,decrease:int):
        if self.balance>=decrease:
            self.balance-=decrease
        else :
            print("not enough balance")
    def show_balance(self):
        print(f"{self.name} balance : {self.balance}")

class Savingaccount(BankAccount):
    def add_interest(self):
         self.balance += self.balance*0.1
         print(self.balance)

a1=BankAccount("ali",500)
a1.deposit(100)
a1.withdraw(200)
a1.show_balance()
s1=Savingaccount("reza",1000)
s1.add_interest()
