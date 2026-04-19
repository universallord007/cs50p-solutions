def main():
    student = get_student()
    # if student[0]== "Clarie":
    #     student[1]="Siliguri"
    if student["name"] == "Clarie":
        student["house"] = "Siliguri"
    print(f"{student['name']} from {student['house']}")
    
# Tuple is immutable, so we cannot change the values of the tuple after it has been created.

def get_student():
    # name = input("Name: ")
    # house = input("House: ")
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student
# By adding square brackets, we can create a list instead of a tuple, which is mutable and allows us to change the values.

if __name__ == "__main__":
    main()