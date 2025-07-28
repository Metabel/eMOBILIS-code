x=10
if x<5:
    print(x,"is less than 5")
    print("code outside of if")
    #if else
    #else
    y=10
    if y<5:
        print(y,"is less than 5")
    else:
        print(y,"is greater than 5")
        
    age=12
    if age>=18:
            print("you are elligible to vote ")
    else:
            print("you are not elligible to vote")
    user_age=(input("Enter your age"))
    if user_age>=18:
                print("you can drive")
    else:
                print("you cant drive")
                
                num=int(input("Enter a number to check if even or odd"))
                if num%2==0: # type: ignore
                    print(num,"is an even number")
                else:
                   print(num,"is an odd number")