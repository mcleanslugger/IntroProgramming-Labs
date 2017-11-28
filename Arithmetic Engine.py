##CMPT 120 - Lab #6
##David Siegel
##17-10-2017
###

from graphics import *

def showEnd():
    print("\nThank you for using the Arithmetic Engine...")
    print("\nPlease come back again soon!")

def showTotal(total):
    print("The result is " + str(total) + ".\n")

def showError(component, message):
    component.setTextColor("red")
    component.setText(message)

def showMessage(component, message):
    component.setText(message)

def waitForInput(win, entry):
    while win.getKey() != "Return": pass
    inputStr = entry.getText()
    entry.setText("")
    return inputStr

def GetUserText(win, entry1, entry2):
    while win.getKey() != "Return": pass
    inputStr1 = entry1.getText()
    inputStr2 = entry2.getText()
    return inputStr1, inputStr2

def makeLabel(win, msg, x, y):
    return Text(Point(x,y) , msg).draw(win)

def makeEmptyLabel(win, x, y):
    return makeLabel(win, "", x, y)

def showIntro():
    app = GraphWin("Arithmetic Engine", 400, 200)
    app.setCoords(0, 0, 10, 10)

    makeLabel(app, "Welcome to the Arithmetic Engine!", 5, 9)
    makeLabel(app, "=================================", 5, 8)
    makeLabel(app, "Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.", 5, 7)
    makeLabel(app, "What computation do you want to perform?", 5, 6)

    inputBox = Entry(Point(5,5), 8).draw(app)
    inputBox.setText("")

    cmd = str(waitForInput(app, inputBox))
    app.close()
    return cmd
    

def doLoop():
    while True:
        cmd = showIntro()

        app = GraphWin("Arithmetic Engine", 400, 400)
        app.setCoords(0, 0, 10, 10)

        makeLabel(app, "Enter   the   first  number:", 2, 7)
        inputBox2 = Entry(Point(5,6), 5).draw(app)
        inputBox2.setText("")
        makeLabel(app, "Enter the second number:", 2, 6)
        inputBox1 = Entry(Point(5,7), 5).draw(app)
        inputBox1.setText("")
        result = makeEmptyLabel(app, 5, 4)
        
        if cmd == "quit":
            break

        try:
            num1, num2 = GetUserText(app, inputBox1, inputBox2)
            num1 = int(num1)
            num2 = int(num2)
        except:
            showError(result, "ERROR: You must enter valid integers!")
            continue

        if cmd == "add":
            total = num1 + num2
        elif cmd == "sub":
            total = num1 - num2
        elif cmd == "mult":
            total = num1 * num2
        elif cmd == "div":
            total = num1 // num2
        else:
            raise Exception("ERROR: Invalid command '" + cmd + "'! Exiting...")

        app.close()
        print("The result is " + str(total) + ".")
        entry = str(input("Would you like to perform another command?(y/n) "))
        if entry == "n":
            break
        
    app.close()
    
def main():
    doLoop()
    showEnd()

main()
