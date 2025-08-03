class InsuficientFundsError(Exception):
    pass
    # def __init__(self):
    #     pass

    # def __str__(self):
    #     # return "Insufficient Funds"
    #     pass


class BankAccount:
    def __init__(self, initial_balance):
        self.initial_balance = initial_balance
        self.account_balance = initial_balance

    def deposit(self, amount):
        balance = amount + self.account_balance
        return balance

    def withdraw(self, amount):
        if amount > self.account_balance:
            raise InsuficientFundsError("Insufficient Funds")
        else:
            balance = self.account_balance - amount
            return balance

    def display_balance(self):
        print(f"Current Balance: {self.account_balance}")
        return self.account_balance


# try:
#     account = BankAccount(100)
#     account.withdraw(account)
# except InsuficientFundsError as e:
#     print(e)
