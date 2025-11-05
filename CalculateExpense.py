print(""" NAME: WOSSEN
      Expense Calculator,
      Input your costs and 
      calculate your total Expense \n""")

sum = 0
print("You can exit anytime, by writing 'exit'")
print(" Please state number of items:")
item_num = input()
all_items = {}

if item_num == "exit":
    exit()
    # if not a number?

for i in range(int(item_num)):
    print("item - ")
    item = input()
    # if exit?
    print("cost -")
    cost = input()
    all_items[item] = cost
    sum += int(cost)
    print(f"total is {sum}")
    
for key, value in all_items.items():
    print(key, value)
print(f"   {sum}")