import random

names_string = input("Give me evertbody's names, seperated by a comma.")
names = names_string.split(", ")
print(names)

random_name = random.randint(0, 2)

print(names[random_name])