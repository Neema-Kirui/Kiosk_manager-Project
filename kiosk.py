def login():
    print("=" * 30, "\n             LOGIN  \n", "=" *30)
    owner = input("Enter name of the store owner : ")
    store = input("Enter the name of  the store : ")

    owner = owner.strip().title()
    store = store.strip().title()

    # hardcoded password
    password = 'howdy'

    # saving user password attempts
    attempt = input("Enter your password : ")
    attempt = attempt.strip().lower()

    # comparing user attempt to password, Dont proceed if not correct
    while attempt != password:
        print("Wrong password!")
        attempt = input("Enter your password : ")
    print("Access Granted")

    print(f"Welcome to {store} kiosk, you are served by {owner}")
    return store



def load_inventory():
    try:
        with open('kiosk_inventory.txt', 'r') as my_file:
            for line in my_file:
                line  = line.strip()
                if not line:
                    continue
                name, price, quantity = line.split(',')
                inventory[name] = {
                    "price": float(price),
                    "quantity": float(quantity)
                }
    except FileNotFoundError:
        # if file not found
        pass

def load_sales():
    try:
        with open('sales_log.txt', 'r') as my_file:
            for line in my_file:
                line = line.strip()
                if not line:
                    continue
                customer, product, amount, total = line.split(',')
                sales_log.append({
                    "cust_name": customer,
                    "sale_prod": product,
                    "amount": float(amount),
                    "total": float(total)
                })
    except FileNotFoundError:
        pass

inventory = {}
sales_log = []

# loading inventory from inventory file to inventory dict
load_inventory()

# loading sales from sales log file to  sales_log list
load_sales()

border = "=" * 30


def main_menu():
    store = login()

    print(f"{border}\n{store.upper():^30}\n{border}")
    print(" 1. View Stock \n 2. Add new product \n 3. Restock a product \n 4. Sell a product \n 5. View sales \n 6. Search products \n 7. Exit")
    print()
    choice = input("Enter your choice (1-7): ")

    if not choice.isdigit():
        print("Please enter a valid choice (1-7).!")
        return

    choice_int = int(choice)

    if choice_int < 1 or choice_int > 7:
        print("Invalid choice. Please enter a number between 1 and 7.")
        return
    return choice_int


def save_inventory():
    with open('kiosk_inventory.txt', 'w') as my_file:
        for product_name, details in inventory.items():
            my_file.write(f"{product_name}, {details['price']}, {details['quantity']} \n")


def show_product():
    for product_name, details in inventory.items():
        print(f"|Product : {product_name:<10} Price : {details['price']:<10} Quantity: {details['quantity']}|")

    
def add_product():
    print(f"{border} \n Adding new product: \n{border}")

    # checking if product name is alphabetic, rejecting all else
    product_name = input("Enter the product name : ")
    while not product_name.isalpha():
        print("Enter a valid product name!")
        product_name = input("Enter the product name : ")
    product_name = product_name.strip().lower()

    # checking if product already exists in inventory. if found cancel adding product
    if product_name in inventory: 
        print()
        print(f"{product_name} already exists in inventory. Product not added.")
        return

    # checking if product price is a digit, rejecting all else
    product_price = input("Enter the product price: ")
    while not product_price.isdigit():
        print("Enter a valid price! (Must be a number)")
        product_price = input("Enter the product price: ")
    product_price = float(product_price.strip())


    # checking if product quantity is a digit, rejecting all else
    product_quantity = input("Enter the product quantity: ")
    while not product_quantity.isdigit():
        print("Enter a valid price! (Must be a number)")
        product_quantity = input("Enter the product quantity : ")
    product_quantity = float(product_quantity.strip())

    # creating product in a dict, appending to inventory 
    inventory[product_name] = {
        "price": product_price,
        "quantity": product_quantity
    }

    # calling save inventory to save product to inventory file
    save_inventory()

    print()
    print(f"{product_name} added to inventory.")
    

def restocking():
    # print(f"{border}\n{store.upper():^30}\n{border}")
    print(f"{border} \n Restocking product:\n{border}")
 

    product_name = input("Enter the product to restock: ")
    # validating product name
    while not product_name.isalpha():
            print("Enter a valid product name!")
            product_name = input("Enter the product name : ")
    product_name = product_name.strip().lower()

    # checking if product in inventory
    if product_name not in inventory:
        print(f"{product_name} not found in inventory.")
        return

    # validating quantity
    restock_quantity = input(f"Enter the quantity to restock: ")
    while not restock_quantity.isdigit():
        print("Enter a valid quantity! (Must be a number)")
        restock_quantity = input(f"Enter the quantity to restock: ")
    restock_quantity = float(restock_quantity.strip())

    # adding restock to the quantity
    inventory[product_name]["quantity"] += restock_quantity

    # calling save inventory to update inventory file
    save_inventory()
    print()
    print(f"Restocked {restock_quantity} units of {product_name}. New quantity: {inventory[product_name]['quantity']}")


def sell_product():
    print(f"{border} \n Selling product:\n{border}")

    customer_name = input("Enter customer name : ")

    # validating customer name
    while not customer_name.isalpha():
        print("Enter a valid customer name !")
        customer_name = input("Enter customer name : ")
    customer_name = customer_name.strip().lower()

    product_name = input("Enter product name to sell: ")

    # validating product name
    while not product_name.isalpha():
            print("Enter a valid product name!")
            product_name = input("Enter the product name : ")
    product_name = product_name.strip().lower()


    if product_name not in inventory:
        print(f"{product_name} does not exist in inventory.")
        return

    product = inventory[product_name]

    # checking current stock
    available_stock = product["quantity"]
    print(f"{product_name:<10} current stock {available_stock}")

    # checking if sale amount is a digit, rejecting all else
    amount = input("Enter sale amount : ")
    while not amount.isdigit():
        print("Enter a valid amount! (Must be a number)")
        amount = input("Enter sale amount: ")
    amount = float(amount.strip())

    # validating sale amount
    if amount <= 0:
        print("Quantity must be greater than zero.")
        return

    if amount > available_stock:
        print(f"Not enough stock. Only {available_stock} units of {product_name} available.")
        return

    # Enough stock -> process the sale
    price = product["price"]
    total = amount * price

    product["quantity"] -= amount
    print(f"Sold {amount} units of {product_name} for a total of ${total:.2f}.")

    # updating inventory file
    save_inventory()
    
    sale = {
            "cust_name" : customer_name,
            "sale_prod" : product_name,
            "amount" : amount,
            "total" : total
        }

    sales_log.append(sale)


    # writing sale log to a sales_log file
    # using append mode so as not to override data from previous runs
    with open('sales_log.txt', 'a') as my_file:
            my_file.write(f"{customer_name}, {product_name}, {amount}, {total}\n")

           
def view_sales():
    print(f"{border}\n Viewing sales :\n{border}")

    # looping thourh each sale in sales log dict
    for sale in sales_log:
        print(f"|Customer : {sale["cust_name"]:<10} bought : {sale["sale_prod"]:<10} quantity : {sale["amount"]:<10}  Total KSH: {sale["total"]} |")


def search_prod():
    print(f"{border} \nSearching up product :\n{border}")

    product_name = input("Enter the product name to search : ")
    # validating product name
    while not product_name.isalpha():
            print("Enter a valid product name!")
            product_name = input("Enter the product name : ")
    product_name = product_name.strip().lower()

    if product_name not in inventory:
        print(f"{product_name} not found in inventory!")
        return

    details = inventory[product_name]
    print(f"|{product_name:<10}  Price : {details['price']:<10}  Stock : {details['quantity']}|")


def main():
    while True:
        choice_int = main_menu()

        if choice_int == 1:
            show_product()
            continue
        
        if choice_int == 2:
            add_product()
            continue

        if choice_int == 3:
            restocking()
            continue

        if choice_int == 4:
            sell_product()
            continue

        if choice_int == 5:
            view_sales()
            continue

        if choice_int == 6:
            search_prod()
            continue
    
        if choice_int == 7:
            print("Closed the shop. Goodbye!")
            break


main()
