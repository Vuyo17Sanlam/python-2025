# Task 1.1


class Bank_Account:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def display_balance(self):
        return self.balance


# task 1.2
chleo = Bank_Account(101, "chleo", 100_000)
diyali = Bank_Account(102, "diyali", 60_000)
jevan = Bank_Account(103, "javan", 800_000)

# task 1.3
print(chleo.display_balance())
