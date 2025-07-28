#python collection\:list,sets,tuples,dictionary
#dictionary:used to store data in key:value pairs
#key:value
student={
    "name":"andrew",
    "age":20,
    "course":"MIT",
}
print(type(student))
print(student)
#accessing a value
print(student["name"])
#adding new item
student["city"]="Nairobi"
print(student)
#updating a value
student["age"]="25"
print(student)
#print all keys
print(student.keys())
#print all values
print(student.values())
#items()
print(student.items())
#looping through keys and values
for x,y in student.items():
    print (x,y)

#loop through keys
for z in student.keys():
    print(z)
#loop through values
for m in student.values():
    print(m)