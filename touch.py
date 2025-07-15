name = "ekpo"
name_length =len(name)//2
first_half = name[:name_length]
second_half = name[name_length:]
print(first_half)
print(second_half)

name = "user@domain.com"
name1 = "gmail"
name_length = len(name)//2
first_half =name[:name_length]
second_half = name[name_length:]
print(first_half[:5] + name1 + second_half[4:])
#print(second_half)
