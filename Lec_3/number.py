#This try and except ValueError is used to handle the case if the user inputs a number
# try:
#     x = int(input("Enter a number: "))
#     print(f"x is {x}")

# except ValueError:
#     print("Please enter a valid number.")


def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            pass
main()