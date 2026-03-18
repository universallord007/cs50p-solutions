name = input("What is your name? ")

match name :
    case "Harry" | "Hermione" | "Ron":
        print("You are a Gryffindor!")
    case "Draco":
        print("You are a Slytherin!")
    case _:
        print("I don't know which house you belong to.")