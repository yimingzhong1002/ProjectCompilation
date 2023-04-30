import matplotlib.pyplot as plt


# change a string to float
def change_str_to_float(s):
    return float(s)

# read the budget or price file into a dict
def read_budget_or_prices_file(fn):
    res = dict()
    with open(fn, "r") as f:
        lines = f.readlines()
        for line in lines:
            line_info = line.strip().split(",")
            # print(line_info)
            res[line_info[0]] = change_str_to_float(line_info[1][1:])
    # print(res)
    return res

# print(read_budget_or_prices_file("lab8_budget.txt"))
# print(read_budget_or_prices_file("lab8_prices.txt"))

# read the purchases into a dict
def read_purchases_file(fn):
    res = dict()
    with open(fn, "r") as f:
        lines = f.readlines()
        idx = 0
        while idx < len(lines):
            line = lines[idx].strip()
            if line.startswith("DAY:"):
                day = line[4:]
                res[day] = {}
                idx += 1
                next_line = lines[idx].strip()
                while idx < len(lines) and not next_line.startswith("DAY:"):
                    next_line_list = next_line.split(",")
                    name = next_line_list[0]
                    purchase_list = next_line_list[1:]
                    res[day][name] = purchase_list
                    idx += 1
                    if idx < len(lines):
                        next_line = lines[idx].strip()
                    else:
                        break
    return res

# plot a bar chart using data
def plot_bar(values, names, title, labels):
    plt.bar(names, values, width = 0.6)
    plt.title(title)
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.show()

# update main process
def update_option(budget_dict, price_dict):
    while True:
        update_option = input("Choose your option: (q for quit)")
        if update_option == "B":
            budget_keys = budget_dict.keys()
            print(f"Choose someone's budget to update from {budget_keys}")
            print(f"budget dict before change: {budget_dict}")
            while True:
                name = input("budget to change: (q for quit)")
                if name == "q":
                    break
                if name not in budget_keys:
                    print("Name not in the budget dict, try again.")
                    continue
                else:
                    budget = input("New budget is:")
                    budget_dict.update({name: float(budget)})
                    break
            print(f"budget dict after change: {budget_dict}")
        elif update_option == "P":
            price_keys = price_dict.keys()
            print(f"Choose one item to update from {price_keys}")
            print(f"price dict before change: {price_dict}")
            while True:
                name = input("item to change: (q for quit)")
                if name == "q":
                    break
                if name not in price_keys:
                    print("Item not in the price dict, try again.")
                    continue
                else:
                    price = input("New price is:")
                    price_dict.update({name: float(price)})
                    break
            print(f"price dict after change: {price_dict}")
        elif update_option == "q":
            break
        else:
            print("option is invalid, please try again.")
            continue

# show purchases by day and plot bar chart
def show_purchases_by_day(price_dict, purchase_dict):
    day_total = {}
    for day, purchases in purchase_dict.items():
        totol = 0
        for name, items in purchases.items():
            for item in items:
                totol += price_dict[item]
                
        day_total[day] = totol
    print(day_total)
    plot_bar(day_total.values(), day_total.keys(), "DAY&TOTAL MONEY", ["DAY", "TOTAL MONEY"])

# show purchases by name and plot bar chart
def show_purchases_by_name(price_dict, purchase_dict, show=True):
    person_total = {}
    for day, purchases in purchase_dict.items():
        for name, items in purchases.items():
            if name not in person_total:
                person_total[name] = 0
            for item in items:
                person_total[name] += price_dict[item]
    if show:
        plot_bar(person_total.values(), person_total.keys(), "PERSON&TOTAL MONEY", ["PERSON", "TOTAL MONEY"])
    return person_total

# show all person's spent money along the weekday
def show_name_along_day(price_dict, purchase_dict):
    person_total = {}
    for day, purchases in purchase_dict.items():
        for name, items in purchases.items():
            if name not in person_total:
                person_total[name] = {"Monday": 0, "Tuesday": 0, "Wednesday": 0,
                                      "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}
            for item in items:
                person_total[name][day] += price_dict[item]
    
    for name, data in person_total.items():
        y = data.values()
        x = range(len(y))
        plt.plot(x, y)
        plt.xticks(range(len(y)), labels=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        plt.title(f"money spent along the days")            
        plt.xlabel("Day")
        plt.ylabel("Total spent")
        plt.legend(labels=person_total.keys())
        plt.show()


# read the txt files
budget_path = input("Path to the budget file: ")
price_path = input("Path to the price file: ")
purchase_path = input("Path to the purchase file: ")
# read data in the txt file 
budget_dict = read_budget_or_prices_file(budget_path)
price_dict = read_budget_or_prices_file(price_path)
purchase_dict = read_purchases_file(purchase_path)

# while loop main process
while True:
    # show the menu
    menu_string = """
            U = Update a price or budget
            SB = show all the budgets
            SP1 = show all the prices
            SP2 = show all the purchases
            AP1 = show total purchases by day
            AP2 = show total purchases by person
            AP3 = show spending along the days for each person
            FP = finish all the purchases, show the budget left
            E = End program
            Choose an option:
            """
    print(menu_string)
    menu_option = input("Choose your option:")
    
    # process the data according to the user input
    if menu_option == "U":  # update the price or budget
        update_string = """
            Choose one type to update: 
            P for price; B for budget.
        """
        print(update_string)
        update_option(budget_dict, price_dict)
    elif menu_option == "SB":
        for name, budget in budget_dict.items():
            print(f"{name}'s budget is {change_str_to_float(budget)}")
        plot_bar(budget_dict.values(), budget_dict.keys(), "Budget&Name", ["name", "budget"])
    elif menu_option == "SP1":
        for item, price in price_dict.items():
            print(f"{item}'s price is {change_str_to_float(price)}")
        plot_bar(price_dict.values(), price_dict.keys(), "price&item", ["price", "item"])
    elif menu_option == "SP2":
        for day, purchases in purchase_dict.items():
            print(f"Today is {day}")
            for name, items in purchases.items():
                print(f"{name} buys {items}")
    elif menu_option == "AP1":
        show_purchases_by_day(price_dict, purchase_dict)
    elif menu_option == "AP2":
        person_total = show_purchases_by_name(price_dict, purchase_dict)
        print(person_total)
    elif menu_option == "AP3":
        show_name_along_day(price_dict, purchase_dict)
    elif menu_option == "FP":
        person_total = show_purchases_by_name(price_dict, purchase_dict, False)
        left_budget = {}
        for name, budget in budget_dict.items():
            left_budget[name] = budget_dict[name] - person_total[name]
        print(left_budget)
        plot_bar(left_budget.values(), left_budget.keys(), "NAME&LEFT", ["Name", "Budget left"])
    elif menu_option == "E":  # break the while loop
        break
    else:  # input is invalid, ask user input again
        print("option is invalid, please try again.")
        continue