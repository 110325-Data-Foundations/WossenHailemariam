print(""" NAME: WOSSEN
      Expense Calculator,
      Input your costs and 
      calculate your total Expense \n""")

print("You can exit anytime, by writing 'exit'")


sum = 0
all_items = {}

def get_input(prompt):
    input_value = input(prompt)
    if input_value.lower() == "exit":
        print("Exiting...")
        exit()
    return input_value

item_num = get_input(" Please state number of items:")
    
if not item_num.isdigit():
    print("Please enter an integer number!")
    exit()

for i in range(int(item_num)):
    item = get_input("item - ")
    cost = get_input("cost - ")
 
    if not cost.isdigit():
        print("Please enter an integer number!")
        exit()

    all_items[item] = cost
    sum += int(cost)
print("---------------------------")
for key, value in all_items.items():
    print(key, value)
print("-------------")
print(f"Total = {sum}")