from tabulate import tabulate

# Creating class with the asked parameters
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # method in the class to return the cost
    def get_cost(self):
        return self.cost

    # method in the class to return the quantity
    def get_quantity(self):
        return self.quantity

    # method to return the object as string including tabulate to format the results on screen
    def __str__(self):
        table = [[f"Country: {self.country}"],[f"Code: {self.code}"],[f"Product: {self.product}"],
        [f"Cost: {self.cost}"],[f"Quantity: {self.quantity}"]]
        return(tabulate(table))

# new list
shoe_list = []

# function that opens inventory file and turns lines into objects, then appends object to list
def read_shoes_data():
    try:
        shoes_file = open("inventory.txt", "r", encoding="utf-8")
        shoe_file = shoes_file.readlines()[1:]
        for line in shoe_file:
            line = line.strip("\n")
            line = line.split(",")
            obj_line = Shoe(line[0], line[1], line[2], line[3], line[4])
            shoe_list.append(obj_line)
            shoes_file.close()
    except FileNotFoundError:
        print("File does not exist.")

# function that asks user to input new item and creates an object from it, then adds it to the list
def capture_shoes():
    country = input("Enter country of manufacturing: ")
    code = input("Enter shoe code: ")
    product = input("Enter product information: ")
    cost = input("Enter cost of item: ")
    quantity = int(input("Enter quantity: "))
    new_object = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_object)
    print("Product added.")

# function that shows all items in list
def view_all():
    for i in shoe_list:
        print(i.__str__())

# function that finds the item with the lowest quantity, then asks user if they want to restock
# if yes asks for additional items and adds them to the quantity in list
# then saves new data to inventory file
def re_stock():
    lowest = min(shoe_list, key=lambda i: int(i.quantity))
    print("\nThe item with the lowest stock is:\n")
    print(lowest)
    update = input("\nWould you like to update the stock for this item? y/n: ").lower()
    if update == "n":
        exit
    elif update == "y":
        add_quantity = int(input("Add number of items to stock: "))
        lowest.quantity = int(lowest.quantity) + add_quantity
        print(f"New quantity is: {lowest.quantity}")
    else:
        print("Wrong input.")
    shoes_file = open("inventory.txt", "w", encoding="utf-8")
    shoes_file.write("Country,Code,Product,Cost,Quantity\n")
    for i in shoe_list:
        shoes_file.write(f"{i.country},{i.code},{i.product},{i.cost},{i.quantity}\n")
    shoes_file.close()

# function that asks user for shoe code and finds item with this code in the list
def search_shoe():
    while True:
        search_shoe = input("Enter product code to search: ").upper()
        for shoe_code in shoe_list:
            if shoe_code.code == search_shoe:
                print("\nCountry,Code,Product,Cost,Quantity")
                print(shoe_code)

# function that returns all items with their value
def value_per_item():
    print("\nCountry,Code,Product,Cost,Quantity,Total value\n")
    for i in shoe_list:
        value = int(i.get_cost()) * int(i.get_quantity())  # int(i.cost) * int(i.quantity)
        print(f"{i.country},{i.code},{i.product},{i.cost},{i.quantity},{value}")


# function that finds the maximum quantity of item from the list
def highest_qty():
    hi_quant = max(shoe_list, key=lambda q: int(q.quantity))
    print("\nItem on sale: \n")
    print(hi_quant)


# ==========Main Menu=============
# reading file data from the file to the list, asking user for input
# and calling matching function for each menu option
read_shoes_data()
while True:
    print("\nPlease choose an option from the menu\n")
    main_menu = input('''View all products - VA\nAdd new product - AP\nView low stock - VL\nSearch product - SP\nView value - VV
View high stock - VH: ''').lower()
    if main_menu == "va":
        view_all()
    elif main_menu == "ap":
        capture_shoes()
    elif main_menu == "vl":
        re_stock()
    elif main_menu == "sp":
        search_shoe()
    elif main_menu == "vv":
        value_per_item()
    elif main_menu == "vh":
        highest_qty()
    else:
        print("Non existing option.")
