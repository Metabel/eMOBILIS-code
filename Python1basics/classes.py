#oop-object oriented programming
#classes-is a blueprint
#attributes:student class:height, name,age,course
#object-is an instance of a class
class Student:
    
    def __init__(self,first_name,last_name,age,course):
        self.first_name =first_name
        self.last_name =last_name
        self.age =age
        self.course =course
        #returns a string when you print the object
    def __str__(self):
        return f'{self.first_name},{self.last_name},{self.age},{self.course}'
    #a function that display student name and course
    def display_info(self):
        return f"The student is {self.first_name},and is learning {self.course}"
    #a method to return fullname
    def fullname(self):
        return f"{self.first_name},{self.last_name}"
    #method to return email
    def get_email(self):
        return f"{self.first_name},{self.last_name}@emobilis.ac.ke"
    #method to return course
    def get_course(self):
        return f"{self.course}"
#create an object
st1=Student("Jane", "Paul","20", "cybersecurity") 
st2= Student("Mary", "Jane","22", "software_development") 
student3= Student("James", "Fuller","25", "data science") 
print(st1)
print(st2)
print(student3)      
#calling the display info method
print(st1.display_info()) 
print(student3.display_info())
#calling the fullname method
print(st1.fullname())
#calling the get_email()method
print(st1.get_email())
#calling the course method
print(st2.get_course())