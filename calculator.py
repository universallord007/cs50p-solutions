# x = float(input("What is the value of x ? "))
# y = float(input("What is the value of y ? "))
# z = (x/y)
# print(f"{z:.2f}")


def main():
    x=int(input("What is the value of x ? "))
    print("The value of x squared is",square(x))


def square(a):
    return a*a


main()