#lists is ordered collection of items. Lists are changeable
#mylist=[listitem1,listitem2,...]
students=["Mark"," dennis", "cate", "Lucy", "Peter"]
print(students)
#accessing list items:use index
print(students[0])
print(students[2])
print(students[4])
#changing list item
students[0]="Luke"
students[1]="Elizabeth"
print(students)
#looping through the list
for x in students:
    print(x)
#list methods().apend().insert().remove(),sort()
#append()adds an items to the end
students.append("george")
print(students)
#remove()-removes an item
students.remove("Lucy")
print(students)
#pop()-removes last item
students.pop()
print(students)
#sort()-sorts in alphabetical order
students.sort()
print(students)
#len()-returns the length
print(len(students))
#create a list of numbers
mynumbers=[12,34,23,67,89,90]
print(mynumbers)
#print numbers greater than 30
for z in mynumbers:
     if z>=30:
         print(z)
#create a list of countries
#print the first and last country
#replace the third country
#sort list 
countries=["Spain","Italy","France"]
print(countries)
countries[0]="Spain"
countries[2]="France"
print(countries)
countries[2]="uk"
print(countries)
countries.sort()
print(countries)


