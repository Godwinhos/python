record = "james, J, 1500000.5, NG0921, 150000.050"


print("Salary slip \n----------")
'''
print("name:   \tjames\t")
print("initials: \tJ\t")
print("ID: \tNG0921\t")
print("Valid ID: \tYES00000\t")
print("Monthly Salary \t#15,000.050\t")
'''
record_of_list = record.split(",")
name = record_of_list[0]
initials = record_of_list[1]
ID = record_of_list[2]
valid_ID = record_of_list[3]
Monthly_salary = float( record_of_list[4])
print(f" name\t{name.capitalize()}\t")
print(f" initials\t{initials}\t")
print(f" ID\t{ID}\t")
print(f" Valid_ID\t{valid_ID}\t")
print(f" Monthly_salary\t#{Monthly_salary:,.2f}\t")


#2nd
print("message\n------------")
message = "GhostNet#X44CR#98.654#TRC8821"
message_of_list = message.split("#")
code_name = message_of_list[0]
message_code = message_of_list[1]
last_letter = message_of_list[1]
Trace_ID = message_of_list[3]
name = "yes"
Severity_Level = float(message_of_list[2])
print(f"code_name\t{code_name}\t")
print(f"message_code\t{message_code}\t")
print(f"last_letter\t{last_letter[4]}\t")
print(f" Trace_ID\t{Trace_ID}\t")
print(f" Traceable\t{name.capitalize()}\t")
print(f" Severity_Level\t{Severity_Level:.2f}\t")
