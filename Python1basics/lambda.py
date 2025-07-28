#lambda function is an anonymous function(no name)
#lambda arg:expression
def add(x,y):
    return x+y
#lambda function that adds two numbers
add=lambda x,y:x+y
print(add(20,30))
#lambda function that multiplies two numbers
prod=lambda a,b:a*b
#calling the function
print(prod(35,56))
#lambda function that adds three numbers
add3=lambda a,b,c:a+b+c
print(add3(30,487,685))

#lambda function that multiplies three numbers
multiply= lambda x,y,z:x*y*z
print("the product of 3 numbers",multiply(20,60,80))

