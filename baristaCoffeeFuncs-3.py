# Functions (have at least 4 functions)
# Project 2: Barista Coffee Assistant
#
# Name: Joanna Chou
# Section: 07
# Date: 1/29/2022
#

#Function 1: Purpose Statement: This function allows the user to enter the type of coffee they want and verfies the validity of the type.
#Signature: None -> str
def type_of_coffee():
    coffees = ["americano", "flat white", "latte", "espresso"]
    user_type = (input("What coffee type would you like? "))
    count_wrong = 1
    while (user_type.lower()) not in coffees and count_wrong < 3:
        count_wrong += 1
        print ("Can you please try again?")
        user_type = (input("What coffee type would you like? "))
    if count_wrong >= 3:
        print("Sorry, we cannot help you here.")
        exit()
    else:
        return user_type.title()


#Function 2: Purpose Statement: This function allows the user to choose if they would like milk on the side and verfies the validity of their response.
#Signature: str -> str
def milk_on_side(user_type):
    if user_type == "Americano" or user_type == "Espresso":
        user_milk = (input("Would you like milk on the side [y, n]? "))
        if user_milk.lower() == 'y':
            return ("Milk on the side")
        elif user_milk.lower() == 'n':
            return ("No extras")
        count_wrong = 1
        while (user_milk.lower()) != "y" and (user_milk.lower()) != "n" and count_wrong < 3:
            count_wrong += 1
            print ("Can you please try again?")
            user_milk = (input("Would you like milk on the side [y, n]? "))
        if count_wrong >= 3:
            print("Sorry, we cannot help you here.")
            exit()
    else:
        return ("No extras")


#Function 3: Purpose Statement: This function allows the user to choose the size of their drink.
#Signature: None -> str
def size():
    user_size = (input("What size do you want [Large, Medium, Small]? "))
    sizes = ["large", "medium", "small"]
    count_wrong = 1
    while (user_size.lower()) not in sizes and count_wrong < 3:
        count_wrong += 1
        print ("Can you please try again?")
        user_size = (input("What size do you want [Large, Medium, Small]? "))
    if count_wrong >= 3:
        print("Sorry, we cannot help you here.")
        exit()
    else:
        return user_size.lower()

#Function 4: Purpose Statement: This function allows the user to choose if they would like their order for takeout and verfies the validity of their response.
#Signature: None -> str
def takeout():
    user_takeout = (input("Is your coffee takeout [y, n]? "))
    count_wrong = 1
    while (user_takeout.lower()) != "y" and (user_takeout.lower()) != "n" and count_wrong < 3:
        count_wrong += 1
        print ("Can you please try again?")
        user_takeout = (input("Is your coffee takeout [y, n]? "))
    if count_wrong >= 3:
        print("Sorry, we cannot help you here.")
        exit()
    if (user_takeout.lower()) == 'y':
        return "Takeout"
    else:
        return "In cafe"

#Function 5: Purpose Statement: This function prints the user's order.
#Signature: str str str str -> None
def print_info(user_type, user_milk, user_takeout, user_cost):
    print(user_type)
    print(user_milk)
    print(user_takeout)
    print(("Please pay ${:0.2f}".format(user_cost)), "to the cashier.")

#Function 6: Purpose Statement: This function calculates the cost of the coffee.
#Signature: str str str -> float
def coffee_cost(user_type, user_milk, user_size):
    user_cost = 0
    if user_type.lower() == "flat white":
        if user_size.lower() == "large":
            user_cost += 3.75
        elif user_size.lower() == "medium":
            user_cost += 3.00
        elif user_size.lower() == "small":
            user_cost += 2.95
    elif user_type.lower() == "americano":
        if user_size.lower() == "large":
            user_cost += 3.25
            if user_milk == "Milk on the side":
                user_cost += 0.25
        elif user_size.lower() == "medium":
            user_cost += 2.95
            if user_milk == "Milk on the side":
                user_cost += 0.25
        elif user_size.lower() == "small":
            user_cost += 2.75
            if user_milk == "Milk on the side":
                user_cost += 0.25
    elif user_type.lower() == "espresso":
        if user_size.lower() == "large":
            user_cost += 3.25
            if user_milk == "Milk on the side":
                user_cost += 0.25
        elif user_size.lower() == "medium":
            user_cost += 2.95
            if user_milk == "Milk on the side":
                user_cost += 0.25
        elif user_size.lower() == "small":
            user_cost += 2.75
            if user_milk == "Milk on the side":
                user_cost += 0.25
    elif user_type.lower() == "latte":
        if user_size.lower() == "large":
            user_cost += 4.15
        elif user_size.lower() == "medium":
            user_cost += 3.75
        elif user_size.lower() == "small":
            user_cost += 2.85
    return(user_cost)