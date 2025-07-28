#function is a block of code that runs only when its called
#creating a function
#def functionname():
       #body of the function
#calling the function
#functionname()
def demo():
    print("hello this is a python function")
#calling the function
demo()
#creating a function
def example():
    print("hello goodmorning")
    #calling function
example()
#function with parameter
def greeting(fname):
    print("hola como estas",fname)
    #calling the function
greeting("Marion")
greeting("Amy")
#function with multiple parameters
def safari(name,age):
    print(f"My name is {name} and I am {age} years old")
safari("Mark", 19)
safari("Jamie",23)
#function with default parameter value
safari("peter",30)
safari("Luke",25)
def myfunction(first_name,course="mit"):
    print("My name is", first_name, "i am learning" ,course)
    #calling the function
myfunction("Leticia")
myfunction("John","Data science")
#function that calculates area of rectangle hint a=l*w
def areaofRectangle(l,w):
    print("The area of a rectangle is of length",l,"and width",w,"is",l*w)
#calling the function
areaofRectangle(12,30)
areaofRectangle(60,40)

#function that calculates area of a circle(3.14*r*r)
def areaofacircle(r,):
    print("The area of a circle is of radius",r,"is",3.14*r)
areaofacircle(7)
areaofacircle(14)
#function with keyword