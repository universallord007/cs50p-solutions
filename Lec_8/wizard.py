class Godfather:
    def __init__(self,name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Student(Godfather):
    def __init__(self,name,house):
        super().__init__(name)
        self.house = house


class Professor(Godfather):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject