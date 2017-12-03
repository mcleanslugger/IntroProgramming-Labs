# RobotStore.py
# Author: David Siegel


class Product:
    def __init__ (self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def checkStock(self, amount):
        if self.stock >= amount:
            return True
        else:
            return False

    def totalCost(self, amount):
        return int(self.price) * int(amount)

    def updateStock(self, amount):
        self.stock -= amount


UltrasoundRangeFinder = Product("Ultrasound range finder", 2.50, 4)

ServoMotor = Product("Servo motor", 14.99, 10)

ServoController = Product("Servo controller", 44.95, 5)

Microcontroller = Product("Microcontroller Board", 34.95, 7)

LaserRangeFinder = Product("Laser range finder", 149.99, 2)

Battery = Product("Lithium polymer battery", 8.99, 8)

Items = [UltrasoundRangeFinder, ServoMotor, ServoController, Microcontroller, LaserRangeFinder, Battery]


def handleCashInput():
    print("\nSorry, that is not a valid amount. Please try again.\n")
    main()


def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0, len(Items)):
        if Items[i].stock > 0:
            print(str(i) + ")", Items[i].name,
                  "$", Items[i].price,
                  "with", Items[i].stock, "left in stock.")
    print()


def main():
    try:
        cash = float(input("How much money do you have? $"))
    except ValueError:
        handleCashInput()

    try:
        while cash > 0:
            printStock()

            vals = input("Enter product ID and quantity you wish to buy: ").split(" ")

            if vals[0] == "quit": break

            prodID = int(vals[0])
            count = int(vals[1])
            cost = Product.totalCost(Items[prodID], count)

            if Product.checkStock(Items[prodID], count):
                if cash >= cost:
                    Product.updateStock(Items[prodID], count)
                    cash -= cost
                    print("You have purchased", count, Items[prodID].name + ".")
                    print("You have $", "{0:.2f}".format(cash), "remaining.")
                else:
                    print("Sorry, you can't afford that product.")
            elif Items[prodID].stock < count:
                print("Sorry, we don't have that many units of", Items[prodID].name + ".")
            else:
                print("Sorry, we are sold out of", Items[prodID].name)
    except UnboundLocalError:
        pass


main()
