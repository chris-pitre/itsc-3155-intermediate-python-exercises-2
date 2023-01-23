# Chris Pitre
# Intermediate Python Exercises 2
# Exercise 1
# BankAccount Class

class BankAccount:
    """
    Class to represent a bank account

    ...

    Attributes
    ----------
    account_name : str
        The name of the account
    balance : float
        Balance of the account
    
    Methods
    -------
    deposit(amount)
        Deposits an amount into the account
    withdraw(amount)
        Withdraws an amount from the account
    get_balance()
        Returns a string stating account name and balance
    """
    def __init__(self, account_name, starting_balance):
        """
        Parameters
        ----------
        account_name : str 
            The name of the account
        starting_balance : float
            The starting balance of the account
        """
        self.account_name = str(account_name)
        self.balance = float(starting_balance)

    def deposit(self, amount):
        """
        Deposits an amount into the account

        Parameters
        ----------
        amount : float
            The amount being deposited into the account
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws an amount from the account

        Parameters
        ----------
        amount : float
            The amount being withdrawn from the account
        """
        self.balance -= amount

    def get_balance(self):
        """
        Returns a string stating account name and balance

        Returns
        -------
        str
            "{account_name} has a balance of {balance}"
        """
        return f"{self.account_name} has a balance of {self.balance}"