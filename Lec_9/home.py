students = ["Harry Potter", "Ron Weasley", "Hermione Granger", "Neville Longbottom", "Luna Lovegood"]

# house = []
# for student in students :
#     house.append({"name": student, "house ": "Gryffindor"})

# print(*house, sep=" ")


# house = {student:"Gryffindor" for student in students}

# print(house, sep=" ")


# 


# This is the code using the enumeration and before we have used the for loop directly but using the enumeration we can get the index of the student as well as the name of the student and we can print it in a better way.
for i, student in enumerate(students):
    print(i+1, student)
