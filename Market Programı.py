import time


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        self.add()

    def add(self):
        with open("info.txt", "a") as file:
            file.write(self.name + "," + str(self.price) + "," + str(self.stock) + "\n")
        print("Item added!")

    def update(self):
        with open("info.txt", "w") as file:
            for j in prod_list:
                file.write(j.name + "," + str(j.price) + "," + str(j.stock) + "\n")
        print("Update successful!")

    def add_to_stock(self, piece):
        self.stock += piece
        self.update()

    def discount(self, discount_value):
        self.price -= discount_value
        self.update()

    def reduce_stock(self, reduce_value):
        self.stock -= reduce_value
        self.update()

    def increase_price(self, increase_value):
        self.price += increase_value
        self.update()

    def show_info(self):
        print("""
            Name : {}
            Price : {}
            Stock : {}
        """.format(self.name, self.price, self.stock))


prod = Product("Pill", 1500, 10)
prod2 = Product("Toy", 2000, 20)
prod3 = Product("Hat", 50, 30)
prod_list = [prod, prod2, prod3]
earnings = 0
access = False
auth = ""
while True:
    while not access:
        user = input("Username : ")
        while True:
            try:
                user_password = int(input("Password: "))
                break
            except ValueError:
                print("Only numbers!")
                time.sleep(1)
                continue
        if user == "admin" and user_password == 123:
            print("Welcome admin!")
            auth = "admin"
            access = True
            time.sleep(2)
        elif user == "customer" and user_password == 456:
            print("Welcome to our store!")
            auth = "customer"
            access = True
            time.sleep(2)
        else:
            print("Sorry, it is wrong!")
            time.sleep(2)

    if auth == "customer":
        while True:
            for i in prod_list:
                i.show_info()
            choose = int(input("Which : "))
            buy = int(input("How many items : "))
            time.sleep(2)
            prod_list[choose - 1].reduce_stock(buy)
            earnings += prod_list[choose - 1].price * buy
            print("Thanks!")
            cont = input("Would you like to continue ? (y, n): ")
            if cont == "y":
                continue
            elif cont == "n":
                print("See you!")
                access = False
                auth = ""
                break
    elif auth == "admin":
        while True:
            print("""
                earnings : {}
                1- Add stock
                2- Reduce stock
                3- Discount
                4- Increase price
                5- Show all
            """.format(earnings))
            answer = int(input("Choose : "))
            if answer != 5:
                for i in prod_list:
                    i.show_info()
                which_prod = int(input("Which Product : "))

            if answer == 1:
                value = int(input("How many : "))
                prod_list[which_prod - 1].add_to_stock(value)
            elif answer == 2:
                value = int(input("How many : "))
                prod_list[which_prod - 1].reduce_stock(value)
            elif answer == 3:
                value = int(input("How much : "))
                prod_list[which_prod - 1].discount(value)
            elif answer == 4:
                value = int(input("How much : "))
                prod_list[which_prod - 1].increase_price(value)
            elif answer == 5:
                for i in prod_list:
                    i.show_info()

            cont = input("Would you like to continue ? (y/n) : ")
            if cont == "y":
                continue
            elif cont == "n":
                access = False
                auth = ""
                break
