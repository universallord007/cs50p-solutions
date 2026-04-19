import random 

class Hat :
    
    houses =["Siliguri", "Islampur","Kishanganj","Jalpaiguri"]

    @classmethod
    def sort(cls,name):
        print(name, "is in" , random.choice(cls.houses) )

Hat.sort("Harry")