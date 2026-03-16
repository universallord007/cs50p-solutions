# Hello guys this is my python program
# name = input("What is your name ? ").strip().title()
# # print("Hello ",name , sep="///", end="\n")
# # print("Hello,\"friend\"")
# # name = name.strip()
# # # name = name.capitalize()
# # name = name.title()
# # name = name.strip().title()
# first,last = name.split(" ")
# print(f"Hello, {first}")

def main():
    hello()
    name = input("What's your name? ")
    hello(name)


def hello(a="World"):
    print("Hello", a)


main()