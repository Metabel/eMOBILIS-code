#function with return statement
#def functionname(parameters):
#return
def myfunction(x):
    return x*5
#calling the function
result=myfunction(50)#store the returned value in a variable
print(result)
#way 2
print(myfunction(64))
#function that adds two numbers and returns the sum
def addtwoNumbers(num1,num2):
    sum=num1+num2
    return sum
#calling the function
print(addtwoNumbers(20,30))
print(addtwoNumbers(500,400))
mysum=addtwoNumbers(40,60)
print(mysum)
#function that finds maximum of two numbers eg max(num1,num2)
def maximumnum(x,y):
    return max(x,y)
#calling the function
print(maximumnum(10,20))
#function that determines even or odd number(num%2==0)
#prompt users for two numbers from user input, then create function that multiplies the two numbers
first_num=int(input("Enter first number"))
second_num=int(input("Enter second number"))
#functions that mltiplies two numbers
def multiplytwonums(a,b):
    return a*b
#calling the function
result=multiplytwonums(first_num,second_num)
print("The product of",first_num,"and",second_num,"is",result)
#function that determines even or odd number(num%2==0)
def evenodd(z):
    if z%2==0:
        print(z,"is an even number")
    else:
        print(z,"is an odd number")
#calling the function
evenodd(7)
evenodd(16)
evenodd(34)
 #function to find largest of the three numbers
def max3num(m,n,o) : 
    return max( m*n*o)
        
print(max3num(35,70,65))


 
