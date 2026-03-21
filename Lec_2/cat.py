# i = 0
# while i < 3:
#     print("meow")
#     i+=1

#Using for loop 
# for _ in range(3):
#     print("Meow")


# print("meow\n" * 3 , end = "")


# while True :
#     n = int(input("How many times do you want to print meow? "))
#     if n < 0 :
#         continue 
#     else :
#         break 

# for _ in range (n):
#     print("meow")



def main():
    x = get_num()
    meow(x)

    
def get_num ():
    while True :
            n = int(input("How many times do you want to print meow? "))
            if n > 0 :
                return n


def meow(n):
    for i in range(n):
        print("meow")


main()