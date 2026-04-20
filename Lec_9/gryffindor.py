students = [{"name": "Harry", "house": "Gryffindor"},
             {"name": "Hermione", "house": "Gryffindor"},
             {"name": "Ron", "house": "Gryffindor"},
             {"name": "Draco", "house": "Slytherin"},
             {"name": "Luna", "house": "Ravenclaw"}]


# gryffindors = [student["name"] for student in students if student["house"] == "Gryffindor"]


# for gryffindor in sorted(gryffindors):
#     print(gryffindor)



# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"


gryffindor = filter(lambda s : s["house"] == "Gryffindor",students)

for _ in sorted(gryffindor, key=lambda s: s ["name"]) :
    print(_["name"])
