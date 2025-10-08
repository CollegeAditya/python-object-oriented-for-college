class bankAccount:
  def __init__(self, accNum, name, balance):
       self.accNum = accNum
       self.name = name
       self.balance = balance
  
  def deposit(self, amount):
       self.balance = self.balance + amount
  
  def withdraw(self, amount):
       if amount > self.balance:
           print("withdraw amount can not be greater than current balance. current balance: ", self.balance)
       else:
           self.balance = self.balance - amount

  def fees(self):
    if self.balance < 1200:
      fees = (5*self.balance)/100
    else:
      fees = None
  
  def details(self):
       print(f"Account Number: {self.accNum}\nName: {self.name}\nBalance: {self.balance}")
