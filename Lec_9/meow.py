# MEOWS = 3
# MEOWS = 4
# for _ in range(MEOWS):
#     print("Meow !!!!")



class Cat :
    MEOWS = 3

    def meow(self):
        for _ in range(self.MEOWS):
            print("Meow !!!!")

cat = Cat()
cat.meow()