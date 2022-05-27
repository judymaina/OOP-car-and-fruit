
class Student:
    School="Akirachix"
    def __init__(self,firstname,secondname,age,Country):
        self.firstname=firstname
        self.secondname=secondname
        self.age=age
        self.Country=Country
    def greeting(self):
        return f"Hello{self.firstname} from{self.Country}welcome to{self.School}"    
    def fullname(self):
        return f"Hello{self.firstname} {self.secondname}:"
    def year_of_birth(self):
        year=2022-self.age
        return f"Hello{self.firstname},you were born in{year}" 
    def initials(self):
         return f"Hello your initial is {self.firstname[0]}{self.secondname[0]}"


