


def hello(name,age):
   year=(2022-age)
   print(f"Hello{name},you were born in {year}")

def hello(name,age): 
     year=(2022-age)

     return f"Hello{name},you were born in {year}"

def add (a,b):
      answer=a+b
      return answer

def my_country(country="Uganda",student="judy"):
   return f"Hello {student} you are from {country}"
def great_multiple(*names):
   for name in names:
      print(f"Hello {name}")
def add(*sum):
   plus=0
   for addition in sum:
      plus+=addition
      return(plus)

def great_multiple(**kwargs):
   print(kwargs.keys())
   print(kwargs.values())

def great_multiple(**kwargs) :
   keys=kwargs.keys() 
   if"country"in keys:
      print(f"Hello {kwargs['name']} you are from{kwargs['country']}")

   elif "age" in keys:
     year=2022-kwargs["age"]
     print (f"Hello{kwargs['name']} you were born in{year}")
   elif not kwargs:
      print(f"Hello Anonymous")  
def sum_and_greet(*args,**kwargs):
   sum=0
   for num in args:
      sum+=num
      keys=kwargs.keys()
      if "name"in keys:
         print(f"Hello{kwargs['name']},the answer is {sum}")
      elif"country"in keys:   
         
         print(f"Hello from{kwargs['country']},the answer is {sum}")
      elif not kwargs:
         print(f"Hello anonymousthe answer is {sum}")

 




       

