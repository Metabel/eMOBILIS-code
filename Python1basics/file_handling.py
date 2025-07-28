#open(filename,mode)
#modes=r-read,a-append,,w-write,x-creates
#write 
x=open("myfile.txt","w")
x.write("hello this is my first file \n")
x.close()
#append
x=open("myfile.txt","a")
x.write("this is appended text\n")
x.close()
#read
x=open("myfile.txt","r")
print(x.read())
x.close()
#create a file demo.txt

#write some data into it
x=open("mydemo.txt","w")
x.write("I can add text on this file\n")
x.close()
#read the contents
x=open("mydemo.txt","r")
print(x.read())
#append some data
x=open("mydemo.txt","a")
x.write("this is appended text\n")
x.close()