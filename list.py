'''
my_list = [ 1,2,3,4]
my_list.extend([5,6,7,8,9])
print(my_list)
my_list.remove(3)
my_list.insert(2,15)
my_list.reverse()
my_list.append(3)
my_list.extend([10])
print(my_list)

my_list = 1,2,3,4
my_list_length = len(my_list)//2
first_half = my_list[:my_list_length]
print(first_half)

message = "hello world"
for char in message:
	print(char)

name = "godwin benjamin"
for char in name.capitalize():
	print(char)

var = 1,2,3,4,5
for num in var:
	if num % 2 == 0:
		print("even")
	else:
		print("odd")
'''

#for i in range(1,100):
#	if i % 2 == 0:
#		print(f" {i}")
#	else:
#		print(f"{i} is odd")








'''
for i in range(1,100):
	if i % 2 == 0:
		print(f" this {i} is even")
'''


num = [1,2,3,4]
print(num)
num.extend([5,6,7,8])
print(num)
