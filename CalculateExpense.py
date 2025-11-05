print(""" NAME: WOSSEN
      Expense Calculator,
      Input your costs and 
      calculate your total Expense \n""")

sum = 0
print("You can exit anytime, by writing 'exit'")
print(" Please state number of items:")
item_num = input()

if item_num == "exit":
    exit()

for i in range(int(item_num)):
    print("item - ")
    item = input()
    print("cost -")
    cost = input()
    sum += int(cost)
    print(f"total is {sum}")
    
