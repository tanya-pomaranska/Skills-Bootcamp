"""
Valentina wants to develop a specialised online shopping cart application 
for pet-related products to simplify her life. Your task is to create the backend 
functionality for her online shopping cart.
Simple Python online shopping cart application. Users should be able 
to view and remove items from their cart, as well as determine the total cost 
of the items.

Challenge: Develop a shopping cart application, called Paws n Cart, 
for pet-related products to help manage your products and that can provide 
information on adoption centres and pet care advice.

Objective: Develop a program to:
- Create a shopping cart for a user which they can view
- Allow users to add and remove items from their cart
- Calculate the total cost of the cart when requested

"""
# Notes: 
# Use the following username and password to access the admin rights 
# username: Kate
# password: password

from tabulate import tabulate

# --- Lists --- #
# List for items you can pay.
list_of_items = [
    {"product name": "Acana Adult Dog Food", "price": 20.56, "info": "350g"},
    {"product name": "Wagg Active Goodness Chicken", "price": 11.99, "info": "400g"},
    {"product name": "Hill's Dog Food", "price": 39.70, "info": "350g"},
    {"product name": "Bones Biscuits Dog Treats", "price": 15.96, "info": "400g"},
    {"product name": "Dreamies Cat Treats Chicken 350g ", "price": 9.96, "info": "350g"}
]
# List of products which user buy
user_basket = []

user_information = [
    {"name": "Kate", "surname": "Smith", "password": "password"}
]

# --- Functions --- #
def  show_menu():
    ''' Show menu and user can choose option '''
     
    menu = int(input("Would you like to:\n\
1. Add an Item to your cart\n\
2. Remove an Item from your cart\n\
3. Update Item on your cart\n\
4. Checkout \n\
Enter the number of the option \n\
:"))
    if menu == 1:
        add_item()
    elif menu == 2:
        remove_item()
    elif menu == 3:
        update_item()
    elif menu == 4:
        print("Goodbye! Have a good day!")
        exit()
    else:
        print("Invalid option picked, try again!!!!!")

def add_item():
    '''Add item to user busket''' 
     
    print("Adding product to basket\n")
    print(f"=========All Products=========\n")
    # Show all items for sail
    display_all_items(list_of_items)

    # Giving chance to user back to main menu
    choice = input("Do you want to continue adding the product to your basket? \n\
Yes - y, No - n Your choice: ").lower() 
    if choice == 'n':
        return show_menu()
    elif choice == 'y':
        # Adding a new item with input validation
        while True:
            try:
                item_index = int(input("\nWhat item do you want to buy.\n\
Please enter the index of item: "))
                # Check if item index is not out of range
                if item_index in range(-len(list_of_items), len(list_of_items)):
                    item_count = int(input("How many item do you want to buy: "))
            
                    new_item = {"product id": item_index, "count": item_count}
                    user_basket.append(new_item)
                    # Show added item
                    print(f"\nThis item has been added\n\
Product:\t{list_of_items[item_index]['product name']} \
{list_of_items[item_index]['info']}\n\
Quantity:\t\t{item_count}\n\
Price:\t\t{list_of_items[item_index]['price']}\n\
Summ:\t\t{round(item_count * list_of_items[item_index]['price'],2)} GBP\n")
                    break
                else:
                    print("Sorry, no items with this index")
                    continue
                    
            except Exception as err_msg:
                print("\n!!! You enter the wrong choice, Please enter the number")
                print(f"{ err_msg }\n")
                continue
        # Show user basket
        display_user_basket()

def remove_item():
    ''' Delete item that choose user '''

    if not user_basket:
        print("\nYour busket is empty.\nProgram can not delete products from empty basket.\n")
    else:
        print("\nDelete product from basket\n")
        # Show user basket
        display_user_basket()

        # Giving chance to user back to main menu
        choice = input("Do you want to continue deleting item from your basket? \n\
Yes - y, No - n Your choice: ").lower() 
        if choice == "n":
            return show_menu()
        elif choice == "y":
            # Adding a new item with input validation
            while True:
                try:
                    item_index = int(input("\nWhat item do you want to delete.\n\
Please enter the index of item: "))
                # Check if item index is not out of range
                    if item_index in range(-len(list_of_items), len(list_of_items)):
                        user_basket.pop(item_index)
                        print("Your item has been deleted from your basket.\n")
                        break
                    else:
                        print("Sorry, no items with this index")
                        continue
                    
                except Exception as err_msg:
                    print("\n!!! You enter the wrong choice, Please enter the number")
                    print(f"{ err_msg }\n")
                    continue
        # Show user basket
        display_user_basket()

def update_item():
    ''' Update the quantity of products chosen by a user in the user basket '''
    if not user_basket:
        print("\nYour busket is empty.\nProgram can not update products from empty basket.")
    else:
        # Show user basket
        display_user_basket()
        # Giving chance to user back to main menu
        choice = input("Do you want to continue update quantity of product? \n\
Yes - y, No - n Your choice: ").lower() 
        if choice == "n":
            return show_menu()
        elif choice == "y":
            # Adding a new item with input validation
            while True:
                try:
                    item_index = int(input("\nWhat item do you want to update.\n\
Please enter the index of item: "))
                # Check if item index is not out of range
                    if item_index in range(-len(list_of_items), len(list_of_items)):
                        new_amount = int(input("Please enter new quantity of this item: "))
                        user_basket[item_index]['count'] = new_amount
                        print(f"The quantity of item {item_index} has been updated.\n")
                        break
                    else:
                        print("Sorry, no items with this index")
                        continue
                
                except Exception as err_msg:
                    print("\n!!! You enter the wrong choice, Please enter the number")
                    print(f"{ err_msg }\n")
                    continue
    # Show user basket
    display_user_basket()

def display_all_items(list_for_display):
    ''' Create a table with Row Index '''
    print(tabulate(list_for_display, headers="keys", showindex="always", tablefmt='fancy_grid'))

def display_user_basket():
    ''' Show user basket ''' 
    if not user_basket:
        print("Your busket is empty.\nPlease add products to your basket to see it.")
    else:    
        # Create list of products
        basket = []
        summary = 0
        for item in user_basket:
            # Cheking if the item belong to this use
            basket.append([list_of_items[item["product id"]]["product name"], 
                            list_of_items[item["product id"]]["info"],
                            item["count"],
                            list_of_items[item["product id"]]["price"],
                            f"{round(item['count'] * list_of_items[item['product id']]['price'],2)} GBP"])
            summary += round(item['count'] * list_of_items[item['product id']]['price'],2)
        # Create table for user busket
        print("Your basket")
        headers = ["Product name", "Info", "Qty", "Price", "Summ"]
        print(tabulate(basket, headers, showindex="always", tablefmt='fancy_grid'))
        print(f"Total: {summary} GBP\n")

# ======== Start program ========
logged_in = False
user_id = None

while not logged_in:
    # Login user
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")

    for id,user in enumerate(user_information):
        if curr_user not in user.values():
            print("User does not exist")
            continue
        elif user["password"] != curr_pass:
            print("Wrong password")
            continue
        else:
            print("Login Successful!\n")
            print(f"Hello {user['name']}!")
            user_id = id
            logged_in = True

# ====== Main part =========
print("Welcome to Paws n Cart shopping cart app!\n")
print(f"{'-'  *  50}")
print("This is your shopping cart")
print(f"{'-'  *  50}")

while True:
    show_menu()