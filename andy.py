data = "0x2f#Trc20#id#send#Trc20405"


print("-----report-----\n")
data_of_list = data.split("#")
address = data_of_list[0]
network = data_of_list[1]
ID = data_of_list[2]
state = data_of_list[3]
Tx_no = data_of_list[4]
print(f"address\t{address}\t")
print(f"network\t{network}\t")
print(f"ID\t{ID}\t")
print(f"state\t{state}\t")
print(f"Tx_no\t{Tx_no[5:7]}\t")

name = "godwinos"
name_length = len(name)//2
first_half = name[:name_length]
second_half = name[name_length:]
print(first_half[0:3])
print(second_half)
