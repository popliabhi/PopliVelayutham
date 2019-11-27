# Model.py
class Breed:
    def __init__(self, id, name, temperament, coat):
        self.id = id
        self.name = name
        self.temperament = temperament
        self.coat = coat

    def display(self):
        print(self.id)
        print(self.name)
        print(self.temperament)
        print(self.coat)
        


class Pupper:
        def __init__(self, name, sex, weight, height, color, birthdate,breedObj):
            self.name = name
            self.sex = sex
            self.weight = weight
            self.height = height
            self.color = color
            self.birthdate = birthdate
            self.breedObj = breedObj
        
        
        def display(self):
            print(self.breedObj)
            print(self.name)
            print(self.sex)
            print(self.weight)
            print(self.height)
            print(self.color)
            print(self.birthdate)
            
        
