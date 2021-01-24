import csv
import os
def save(p):
    if os.path.exists("products.csv"):
        os.remove("products.csv")
    with open("products.csv", mode="w", newline="") as f:
        writer=csv.writer(f, delimiter=",")
        for product, price in p.items():
            writer.writerow([product, price])

def load(p):
    if os.path.exists("products.csv"):
        with open("products.csv", mode="r") as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                p[row[0]]=format(float(row[1]),'.2f')

def admin_mode(p):
    req=5
    while req!=0:
        print("Add a product.......1")
        print("View products.......2")
        print("Edit product price.......3")
        print("Remove a product.......4")
        print("Save changes.......5")
        print("Quit.......0")
        try:
            req=int(input("Enter a number  "))
        except:
            print("Please enter a number")
            req=6
        if req == 1:
            product = input("Enter product name    ")
            if product in p.keys():
                print("Product already exists")
            else:
                try:
                    price = float(input("Enter the per unit price for {}   ".format(product)))
                    if price>=0:
                        p[product]=format(price, '.2f')
                        print("Added {} with unit price ${}.".format(product, p[product]))
                    else:
                        print("Please enter a valid price")
                except:
                    print("Please enter a valid price")
        elif req == 2:
            print("Product\t\tPrice\n")
            for product, price in p.items():
                print("{}\t\t${}".format(product, price))
        elif req == 3:
            product = input("Enter product name    ")
            if product in p.keys():
                try:
                    price = float(input("Enter the per unit price for {}   ".format(product)))
                    if price>=0:
                        p[product]=format(price, '.2f')
                        print("Changed the unit price of {} to ${}.".format(product, p[product]))
                    else:
                        print("Please enter a valid price")
                except:
                    print("Please enter a valid price")
            else:
                print("Product does not exist")
        elif req == 4:
            product = input("Enter product name    ")
            try:
                del p[product]
                print("Deleted {}".format(product))
            except:
                print("Product does not exist")
        elif req == 5:
            save(p)
        else:
            print("Please enter a number 0-4")

def customer(p, n):
    print("Welcome {}!".format(name))
    cart={}
    req=4
    while(req!=0):
        print("Add an item to the cart.......1")
        print("View your cart.......2")
        print("Remove an item from the cart.......3")
        print("Quit.......0")
        try:
            req=int(input("Enter a number  "))
        except:
            print("Please enter a number")
            req=4
        if req == 1:
            product = input("Enter product name    ")
            if product in p.keys():
                print("{} costs ${} per unit".format(product, p[product]))
                try:
                    num = int(input("Please enter the number of {} you wish to purchase    ".format(product)))
                    if(num>=1):
                        if product in cart.keys():
                            cart[product] = cart[product] + num
                        else:
                            cart[product]=num
                        print("Added {} {} to your cart".format(num, product))
                    else:
                        print("Please enter a valid number")
                except:
                    print("Please enter a valid number")
            else:
                print("{} not sold".format(product))
        elif req == 2:
            print("\t\t{}'s shopping cart".format(n))
            print("\nProduct\tQuantity\tCost\n")
            total=0.0
            for product, num in cart.items():
                c = float(float(p[product]) * int(num))
                total = float(total) + c
                print("{}\t{}\t{}\t".format(product, num, format(c, '.2f')))
            print("\nTotal: {}\n".format(format(total, '.2f')))
            print("Thank you for shopping with us!")
        elif req == 3:
            product = input("Enter product name    ")
            if product in cart.keys():
                try:
                    num = int(input("Please enter the number of {} you wish to remove from your cart    ".format(product)))
                    if(cart[product] >= num):
                        cart[product] = cart[product] - num
                        if(cart[product] == 0):
                            del cart[product]
                        print("Removed {} {} from your cart".format(num, product))
                    else:
                        print("You cannot remove more items than you currently have")
                except:
                    print("Please enter a valid number")
        else:
            print("Please enter a number 0-3")
name=""
products={}
while name!="quit":
    name = input("Enter your name\n")
    load(products)
    if name == "admin":
        admin_mode(products)
    else:
        customer(products, name)