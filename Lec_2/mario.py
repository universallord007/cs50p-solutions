def main():
    x = int(input("How many times row and columns do you want ... Its a square? "))
    print_square(x)


def print_square(n):
    for i in range(n):
        for j in range(n):
            print("#", end="")
        print()


main()