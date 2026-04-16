names = []


# with open("names.txt") as file :
#     for line in file:
#         names.append(line.rstrip())


# for _ in sorted(names):
#     print(f"Hello, {_}")


with open("names.txt") as file :
    for line in sorted(file, reverse=True):
        print(f"Hello, {line.rstrip()}")