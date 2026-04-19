class Vault :
    def __init__(self,galleons=0,sickles=0,knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} galleons, {self.sickles} sickles, {self.knuts} knuts"
    
    def __add__(self,other):
        if not isinstance(other, Vault):
            raise ValueError("Can only add another Vault")
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons,sickles,knuts)
    
potter = Vault(10,5,2)
print(potter)
weasley = Vault(5,10,5)
print(weasley)
add = potter + weasley
print(add)