class Account:
    def __init__(self,name,phone,loan,loan_limit):
          self.name=name
          self.phone=phone
          self.balance =0
          self.transaction=500
          self.loan=0
          self.loan_fees=0.20
          self.loan_limit=loan_limit
    def deposit(self,amount):
        if amount<=0:
            self.balance += amount
            return f" Hello {self.name}.you have deposited{amount}your new balance is{self.balance}"
        else:
           return "please deposit a valid amount"






    def widthdraw(self,amount):
        total=amount+self.transaction
        if amount<=0:
            return "valid amount"
        elif total> self.balance:
            return "insufficient balance"
        else:
            self.balance=total
            return (f" Hello {self.name} you have withdrawn {amount}.your new balance is {self.balance}")


    def borrow(self,amount):
        if self.loan>=0:
            return "your transaction is unsuccessful.pay an existing loan"
        else:
            amount<=self.loan_limit
            self.balance<=amount
            self.loan<=amount
            return( f" your loan is{amount} and you new balance is{self.balance}")
