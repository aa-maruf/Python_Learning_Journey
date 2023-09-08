
class bank:
    
    def __init__(self, balance) :
        self.balance = balance
        self.max_withdraw = 10000
        self.min_withdraw = 500
    
    def get_balance (self):
        return self.balance
    def withdraw (self, amount) :
        if amount < self.min_withdraw:
            return f'Low amount of money. Minimum withdraw amount {self.min_withdraw}'
        elif amount > self.max_withdraw:
            return f'Exceeds max limits.You can\'t withdraw more than {self.max_withdraw}'
        elif amount > self.balance:
            return f'Your balance is low.Insufficient balance.'
        else : 
            self.balance = self.balance - amount
            return f'Withdraw successful. Your current balance is {self.balance}'

my_bank = bank(10000)
reply = my_bank.withdraw(100)
print(reply)
reply = my_bank.withdraw(1000)
print(reply)
reply = my_bank.withdraw(50000)
print(reply)

print(my_bank.get_balance())

        