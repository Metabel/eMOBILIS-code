#with statement
with open("newfile.txt","w")as x:
    x.write("Hello python\n")
    x.write("writing to files in python\n")
    
    #append
with open("newfile.txt","a")as x:
    x.write("this is appended text\n")   
    
#read the file contents
with open("newfile.txt","r")as x:
    print(x.read())
    