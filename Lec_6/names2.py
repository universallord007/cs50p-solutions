with open ("names.txt","r") as file:
#     lines = file.readlines()

# for line in lines:
#     print(f"Hello, {line}")
    for _ in file:
        print("Hello,", _.rstrip())