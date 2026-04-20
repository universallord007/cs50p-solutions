class Account :
    def __init__(self):
        self._balance = 0
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self,n):
        self._balance +=n

    def withdraw(self,n):
        self._balance -=n


def main():
    account = Account()
    print("The initial balance was : ", account.balance)
    account.deposit(100)
    account.withdraw(65)
    print("The currentbalance is : ", account.balance)


if __name__ == "__main__":
    main()