actors = [
    {"name": "House Stark", "house": "England"},
    {"name": "House Lannister", "house": "America"},
    {"name": "House Targaryen", "house": "America"},
    {"name": "House Baratheon", "house": "Scotland"},
]

houses = set()
 
for actor in actors :
       houses.add(actor["house"]) 


for house in sorted(houses):
    print(house)