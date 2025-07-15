'''two variable " magic number
my_age = 100
pi = 3.14159

magic_number = (my_age * 3)
magic_number = (my_age * 3) + pi
print(magic_number % 7)

#create variable secret word
secret_variable = "PythonIsAmazing"
print(secret_variable[:6])
print(secret_variable[8:15])
print(secret_variable[-9:-7])
print(secret_variable[:: -1])

print(secret_variable[::2])

print(secret_variable[:6].upper())
print(secret_variable[6:15].lower())
print(secret_variable[:6].upper() + secret_variable[8:15].lower())
'''

'''first_name = "python"
first_name = first_name.capitalize()
print(first_name)

first_name = "python is a general purpose language`"
print(first_name.capitalize())

#first_name = "python"
print(first_name[0].upper() + first_name [1:])


name = input("enter your name ")
result=len(name)
print(result)
'''

weight = float(input("your weight"))
unit = input("input unit, kgs or lbs")
if unit == "k":
	weight = weight * 2.205
	print(weight in lbs)
elif unit == "l":
	weight = weight / 2.205
	print(weight in kgs)






