#elif=used to add another condition to test if the
#if conition if false
"""if..elif..else
if condition
block of code to be executed
elif condition:
block of code to be

else"""
a=5
if a>12:
    print(a,"is greater than 12")
elif a<5:
     print(a,"is less than 5") 
elif a==5:
     print(a,"is  equal to 5")
else:
    print(a,"is not equal to 5")
    #a program that prompts a user for age then checks it
    #18-25-young adult
    #25-4- adult
    #40>-mature adult
    # <18-baby
age=int(input("enter your age"))
if age>=18 and age<25:
        print("you are a young adult")
elif age>=25 and age<40:
        print("you are an adult")
elif age>=40 and age<100:
        print("you are a mature adult")
else:
        print("you are a baby")
        #a program that ask user for marks prints students grade
        #80-100=A
        #70-80=B
        #60-70=C
        #50-60=D
        #<=FAI
marks=int(input("Enter your marks:"))
if marks>=80 and marks<=100:
 print("GRADE A")
elif marks>=70 and marks<80:
 print("GRADE B") 
elif marks>=60 and marks<70:
 print("GRADE C") 
elif marks>=50 and marks<60:
 print("GRADE D") 
elif marks>=0 and marks<50:
  print("FAIL") 
else:
 print("enter a valid numbe between 1 and 100")
   #a program that prompts users for two numbers then prints
   #the larger or if they are equal
    
              
    