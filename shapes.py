
class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        A=3.14*(self.r)*(self.r)
        return f"the area is {A}" 
    def circumference(self):
        c=2*3.14*(self.r)
        return f"the circumference is {c}"  

class Square:
    def __init__(self,a):
        self.a=a
    def area(self):
         A=(self.a)*(self.a)
         return f"the area is {A}"
    def perimeter(self):
        p=4*(self.a)
        return f"the perimeter is {p}" 
class Rectangle:
    def __init__(self,w,l):
        self.w=w
        self.l=l
    def area(self) :
        A=(self.w)*(self.l)
        return f"the area is {A}"
    def perimeter(self):
        p=2*(self.l + self.w) 
        return f"the perimeter is {p}" 
class Sphere:
    def __init__(self,r):
        self.r=r
    def surface_area(self):
        A=(4*3.14)*(self.r)*(self.r)
        return f"the surface area is {A}"
    def volume(self) :
        v=(4/3(3.14(self.r**3)))  
        return f"the volume is {v}" 

    




                


       






