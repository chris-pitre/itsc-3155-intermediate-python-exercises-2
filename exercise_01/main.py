# Chris Pitre
# Intermediate Python Exercises 2
# Exercise 1

import BankAccount

account1 = BankAccount.BankAccount("Chris", 1000)
account1.deposit(20)
account1.withdraw(30)
print(account1.get_balance())