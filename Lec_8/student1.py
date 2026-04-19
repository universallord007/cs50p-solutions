class Student:
    def __init__(self,name,house):
        self.name = name
        self.house = house

    @classmethod   
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name,house)

    def __str__(self):
        return f"{self.name} from {self.house} ."
    # def charm(self):
    #     match self.patronus:
    #         case "Stag":
    #             return "😍"
    #         case "Otter":
    #             return "🦦" 
    #         case "Jack Russell Terrier":                
    #             return "🐶"
    #         case _:
    #             return "🪄"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self,house):
        if house not in ["Siliguri", "Islampur","Kishanganj","Jalpaiguri"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = Student.get()
    # print("Expecto Patronum:", student.charm())
    print(student)
    
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name,house)


if __name__ == "__main__":
    main()