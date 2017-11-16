## RobotStore.py
## Author: David Siegel

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
        return (int(self.price) * int(amount))

    def updateStock(self, amount):
        self.stock -= amount
        
        

productNames = [ Product("Ultrasound range finder", 2.50, 4)
               , Product("Servo motor", 14.99, 10)
               , Product("Servo controller", 44.95, 5)
               , Product("Microcontroller Board", 34.95, 7)
               , Product("Laser range finder", 149.99, 2)
               , Product("Lithium polymer battery", 8.99, 8)
               ]

def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0, len(productNames)):
        if productNames[i].stock > 0:
            print(str(i) + ")", productNames[i].name, "$", productNames[i].price)
    print()

def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()

        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")

        if vals[0] == "quit": break

        prodID = int(vals[0])
        count = int(vals[1])

        if productNames[prodID].stock >= Product.checkStock(productNames[prodID], count):
            if cash >= Product.totalCost(productNames[prodID], count):
                Product.updateStock(productNames[prodID], count)
                cash -= productNames[prodID].price * count
                print("You have purchased", count, productNames[prodID].name + ".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", productNames[prodID])


main()
