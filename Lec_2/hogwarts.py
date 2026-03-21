students = ["Harry", "Hermione", "Ron", "Draco", "Neville"]

# print(students[0])
# print(students[1])
# print(students[2])
# print(students[3])
# print(students[4])

# for _ in range(len(students)-1):
#     print(_+1,students[_])

# for student in students :
#     print(student)



# students = {"Harry": "Gryffindor",
#             "Hermione": "Gryffindor",
#             "Ron": "Gryffindor",
#             "Draco": "Slytherin",
#             "Neville": "Gryffindor"}

# for student in students :
#      print(student,students[student], sep=", ")



# This is the example of using dictionary inside a list 
books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "1984", "author": "George Orwell", "year": None}
]


for book in books :
    print(book["title"],book["author"], book["year"], sep = ", ")