name = input("Whats Your name ?")

# file = open("names.txt","a")
# # file.write(name)
# file.write(f"{name}\n")
# file.close()


with open("names.txt","a") as file:
# file.write(name)
    file.write(f"{name}\n")
    