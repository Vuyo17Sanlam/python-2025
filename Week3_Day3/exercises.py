# Task 1.1


class Bank:
    interest_rate = 0.02
    no_account = 0

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        Bank.no_account += 1

    def display_balance(self):
        return f"Your balance is: {self.balance:,.2f}"

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return (
                f"Insert a correct amount {self.display_balance()}"
                if amount <= 0
                else f"Don't have enough money on your bank account{self.balance:,.2f}"
            )

        self.balance -= amount
        return f"Success. {self.display_balance()}"

    def deposit(self, amount):
        if amount <= 0:
            return f"invalid amount. {self.display_balance()}"
        self.balance += amount
        return f"Successfully deposited. {self.display_balance()}"

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Successfully applied. {self.balance}"

    @classmethod
    def update_interest_rate(cls, new_rate):
        if new_rate <= 0 or new_rate > 100:
            return f"invalid interest rate"
        cls.interest_rate = new_rate / 100
        return f"Successfully updated to {new_rate}%"

    @staticmethod
    def get_total_no_accounts():
        return f"In total the bank has {Bank.no_account}"


class SavingsAccount(Bank):
    interest_rate = 0.05


class CheckingAccount(Bank):
    def withdraw(self, amount):
        return super().withdraw(amount + 1)


chleo = Bank(101, "chleo", 20_000)
anita = SavingsAccount(102, "anita", 20_000)
diyali = CheckingAccount(103, "diyali", 20_000)

print(chleo.apply_interest())
print(anita.apply_interest())
print(diyali.withdraw(1000))
