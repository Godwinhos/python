#about name of a user
name= input("name ")
print(name)

#about age of a user
birth_year = input("enter your birth_year ")
age = 2025 - int(birth_year)
print(age)

#about weight of a user
weight = int(input("weight "))
unit = input("(k)gs or (l)bs ")
if unit.upper () == "K":
	converted =  weight / 0.45
	print("weight in Kgs" + str(converted))
else:
	converted = weight * 0.45
	print("weight in l" + str(converted))

#about height
height = input("height ")
print(height) 

#about hobbies
hobbies = input("hobby1 ")
print(hobbies)

#about marriage
#is_married = "true"
#if is_married:
#	print("married")
#else:
#	print("not married")

is_married = input("are you married? (yes/no)")
if is_married == "yes":
	print("married")
else:
	print("not married")
