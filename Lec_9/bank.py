balance = 0


def main():
    print(f"The initial balance was : {balance}")
    deposit(100)
    withdraw(50)
    print(f"The new balance is : {balance}")

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()

