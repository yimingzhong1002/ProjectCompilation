import matplotlib.pyplot as plt


# read the budget/price file into a dict
def read_prices_file(txt):
    file = dict()
    with open(txt, "r") as f:
        lines = f.readlines()
        for line in lines:
            line_info = line.strip().split(",")
            # print(line_info)
            file[line_info[0]] = convert_str_to_float(line_info[1][1:])
    return file


def read_purchases_file(txt):
    file = dict()
    with open(txt, "r") as f:
        lines = f.readlines()
        position = 0
        while position < len(lines):
            line = lines[position].strip()
            if line.startswith("DAY:"):
                day = line[4:]
                file[day] = {}
                position += 1
                next_line = lines[position].strip()
                while position < len(lines) and not next_line.startswith("DAY:"):
                    next_line_list = next_line.split(",")
                    name = next_line_list[0]
                    purchase_list = next_line_list[1:]
                    file[day][name] = purchase_list
                    position += 1
                    if position < len(lines):
                        next_line = lines[position].strip()
                    else:
                        break
    return file

def convert_str_to_float(s):
    return float(s)

# plot a bar chart using data
def plot_bar(values, names, title, labels):
    plt.bar(names, values, color = 'Pink', width = 0.4)
    plt.title(title)
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.show()

# update main process
def update_option(budget_dict, price_dict):
    while True:
        update_option = input("Choose your option: (exit to go back)")
        if update_option == "B":
            budget_keys = budget_dict.keys()
            print("Choose someone's budget to update from {budget_keys}")
            print("Budget dict before update: {budget_dict}")
            while True:
                name = input("budget to update: (exit to go back)")
                if name == "exit":
                    break
                if name not in budget_keys:
                    print("Person not in the file, try again.")
                    continue
                else:
                    budget = input("New budget is: ")
                    budget_dict.update({name: float(budget)})
                    break
            print(f"budget dict after update: {budget_dict}")
        elif update_option == "P":
            price_keys = price_dict.keys()
            print(f"Choose one item to update from {price_keys}")
            print(f"price dict before update: {price_dict}")
            while True:
                name = input("item to update: (exit to go back)")
                if name == "exit":
                    break
                if name not in price_keys:
                    print("Item not in the file, try again.")
                    continue
                else:
                    price = input("New price is: ")
                    price_dict.update({name: float(price)})
                    break
            print(f"price dict after change: {price_dict}")
        elif update_option == "exit":
            break
        else:
            print("option is invalid, please try again.")
            continue

def show_purchases_by_day(price_dict, purchase_dict):
    day_total = {}
    for day, purchases in purchase_dict.items():
        total = 0
        for name, items in purchases.items():
            for item in items:
                total += price_dict[item]
                
        day_total[day] = total
    print(day_total)
    plot_bar(day_total.values(), day_total.keys(), 
             "Total Purchase By Day", ["Day", "Total Purchase"])

def show_purchases_by_name(price_dict, purchase_dict, show=True):
    person_total = {}
    for day, purchases in purchase_dict.items():
        for name, items in purchases.items():
            if name not in person_total:
                person_total[name] = 0
            for item in items:
                person_total[name] += price_dict[item]
    if show:
        plot_bar(person_total.values(), person_total.keys(), 
                 "Total Purchase By Person", ["Name", "Total Purchase"])
    return person_total


# read the txt files
budget_file = input("Enter budget file: ")
price_file = input("Enter price file: ")
purchase_file = input("Enter purchase file: ")
# read data in the txt file 
budget_dict = read_prices_file(budget_file)
price_dict = read_prices_file(price_file)
purchase_dict = read_purchases_file(purchase_file)

# while loop main process
while True:
    # show the menu
    menu = """
            Correction = Update a budget or a price
            APrices = show all the prices
            APurchases = show all the purchases
            TPD = show total purchases by day
            TPP = show total purchases by person
            budgets_show = show all the budgets
            Select an option:
            """
    print(menu)
    menu_option = input("Choose your option:")
    
    if menu_option == "Correction":  
        update_string = "Select one attribute to correct:\
        B for budget; P for price."
        
        print(update_string)
        update_option(budget_dict, price_dict)
    
    elif menu_option == "APrices":
        for item, price in price_dict.items():
            print(f"{item}'s price is {convert_str_to_float(price)}")
        plot_bar(price_dict.values(), price_dict.keys(), "price&item", ["price", "item"])
    elif menu_option == "APurchases":
        for day, purchases in purchase_dict.items():
            print(f"Today is {day}")
            for name, items in purchases.items():
                print(f"{name} buys {items}")
    elif menu_option == "TPD":
        show_purchases_by_day(price_dict, purchase_dict)
    elif menu_option == "TPP":
        person_total = show_purchases_by_name(price_dict, purchase_dict)
        print(person_total)
    elif menu_option == "budgets_show":
        for name, budget in budget_dict.items():
            print(f"{name}'s budget is {convert_str_to_float(budget)}")
        plot_bar(budget_dict.values(), budget_dict.keys(), "Budget&Name", ["name", "budget"])    
    else:  
        print("option is invalid, please try again.")
        continue