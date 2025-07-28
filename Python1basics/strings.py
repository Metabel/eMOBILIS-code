fname="jane"
course="python"
print(f"my name is {fname} and i am learning {course}")

message="hello how are you"
#string methods .upper(),lower() string.method()
print(message)
print(message.upper())#converts to uppercase
print(message.lower())#converts to lowercase
print(message.title())
#replace(old,new)
print(message.replace("hello","good morning"))
#find()-find the index
myfav="I love Python"
print(myfav.find("python"))
print(myfav.find("I"))
#slicing/substring- is part of a string
#string[start :stop]
text="python"
msg="hello"
print(text[0:4])
print(msg[1:4])
print(text[2:])
print(text[:3])#slice from beginning to 3
#skip characters
print(text[::2])
course="fullstack"
#escape characters \n \t
print("This is a message \n this goes to a new line")
print("name \t:Age")
print("he said \"hello\"")
print("she said \"I love python\"")

print('it\'s a nice day')
print('The student said "hurray"')
print("\"Everyone should learn to code\"""barack Obama")
print("she said\"I am learning python\"")
print("\"It\'s a new day\"""Jane said")



