#here's a fun little trick. Instead of asking for user input twice,
#once before the loop and again inside the loop, it's possible to
#just give a "dummy" value to trick the loop into starting
menu_option = 'X'

#we'll start with an empty list of days (tip: when you're testing,
#you can put some data in here so you don't need to manually add data each
#time, just be sure to set it back to an empty list after you're done)
plastic_removed = []
date = 0
overload = []
threshold = int(input("Enter kg of threshold: "))
#loop until the user chooses to end
while(menu_option != 'E'):
    #another fun hack, if you use a triple quoted (""") string, you
    #can add line breaks and it will still print nicely
    menu_string = """
    A = Add data
    R = Add start and end date
    T = Get Total kg of Plastic Removed
    O = Get Number of Overload Days
    E = End program
    Choose an option:
    """
    menu_option = input(menu_string)

    
    if (menu_option == 'A'):
        date += 1
        while (True):
            plastic_entered = int(input("Enter kg of plastic removed on day " + str(date) + ": "))       
            if str(plastic_entered).isdigit():
                plastic_removed.append(plastic_entered)
                break
            else:
                print("invalid, try again")
                continue
            
        if plastic_entered > threshold:
            overload.append(plastic_entered)
            
        print(plastic_removed)
        print(overload)

    elif (menu_option == 'R'):
        start_date = int(input("Enter start date: "))
        end_date = int(input("Enter end date: "))
        plastic_range = plastic_removed[(start_date - 1):(end_date)]
        total_overloaddays = (overload[(start_date - 1):(end_date)])
        print(plastic_range)
        print(total_overloaddays)
        
    #T = Get Total kg of Plastic Removed, O = Get Number of Overload Days
    
    elif (menu_option == 'T'):
        total_plastic = sum(plastic_removed)
        print(total_plastic)
    
    elif (menu_option == 'O'):
        number_days_overload = len(total_overloaddays)
        print(number_days_overload)
    
    