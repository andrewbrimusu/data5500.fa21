name = "andy"
print(name, id(name))
name = "jonny"
print(name, id(name))
name = "andy"
print(name, id(name))

age = 39
print(age, id(age))
age = 40
print(age, id(age))



# create a dictionary
person = {}
person["name"] = "andy"
person["age"] = 39
person["employer"] = "Utah State University"
person["height_inches"] = 77
person["favorite_movies"] = ["up", "star wars6"]

# access individual elements of a dictionary
print(person["name"])
print(person["age"])

print(person)

# access elements in a loop
for key in person.keys():
    print(key, ":", person[key])
   
 













# checkpoint activity

# Write a program that asks the user the following 
# survey information (a mixture of strings and numbers)
# How many years have you lived in Cache Valley (enter a float)?
# What is your favorite color (enter a string)?
# What is your favorite programming language (enter a string)?

# store the user's answers in a Dictionary
# loop through the dictionary and print all the values








# solution
years = float(input("How many years have you lived in Cache Valley? (enter a float)"))
favorite_color = input("What is your favorite color? (enter a string)")
language = input("What is your favorite programming language? (enter a string)")

personal_info = {}
personal_info["years"] = years
personal_info["color"] = favorite_color
personal_info["lang"] = language

for key in personal_info.keys():
    print(personal_info[key])
    
