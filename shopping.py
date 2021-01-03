
def admin_mode(p):
    req=5
    while req!=0:
        print("Add a product.......1")
        print("View products.......2")
        print("Edit product price.......3")
        print("Remove a product.......4")
        print("Quit.......0")
        try:
            req=int(input("Enter a number  "))
        except:
            print("Please enter a number")
            req=5
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
                try:
                    num = int(input("Please enter the number of {} you wish to purchase    ".format(product)))
                    cart[product]=num
                    print("Added {} {} to your cart".format(num, product))
                except:
                    print("Please enter a valid number")
            else:
                print("{} not sold".format(product))
        elif req == 2:
            print("\t\t{}'s shopping cart".format(n))
            print("\nProduct\tQuantity\tCost\n")
            total=0
            for product, num in cart.items():
                total = total + p[product]*num
                print("{}\t{}\t{}\t".format(product, num, p[product]*num))
            print("\nTotal: {}\n".format(total))
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
                    else:
                        print("You cannot remove more items than you currently have")
                except:
                    print("Please enter a valid number")

name=""
products={}
while name!="quit":
    name = input("Enter your name\n")
    if name == "admin":
        admin_mode(products)
    else:
        customer(products, name)