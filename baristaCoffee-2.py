# Main Program
# Project 2: Barista Coffee Assistant
#
# Name: Joanna Chou
# Section: 07
# Date: 1/29/2022
#
from baristaCoffeeFuncs import *
def main():
    user_type = type_of_coffee()
    user_milk = milk_on_side(user_type)
    user_size = size()
    user_takeout = takeout()
    user_cost = coffee_cost(user_type, user_milk, user_size)
    print_info(user_type, user_milk, user_takeout, user_cost)

    ans = input("Do you want to order another coffee (y/n)? \n")
    while ans == "y":
        user_type = type_of_coffee()
        user_milk = milk_on_side(user_type)
        user_size = size()
        user_takeout = takeout()
        user_cost = coffee_cost(user_type, user_milk, user_size)
        print_info(user_type, user_milk, user_takeout, user_cost)
        ans = input("Do you want to order another coffee (y/n)? \n")


if __name__ == '__main__':
    main()

