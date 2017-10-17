##CMPT 120 - Lab #6
##David Siegel
##17-10-2017
###

def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'\n")

def showOutro():
    print("\nThank you for using the Arithmetic Engine...")
    print("\nPlease come back again soon!")

def doLoop():
    result = 0    
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
        except:
            print("You did not enter valid numbers. Please try again.")
            continue
        
        cmd = input("What computation do you want to perform? ")
        cmd = cmd.lower()

        if cmd == 'add':
            result = num1 + num2
        elif cmd == 'sub':
            result = num1 - num2
        elif cmd == 'mult':
            result = num1 * num2
        elif cmd == 'div':
            result = num1 // num2
        elif cmd == 'quit':
            break
        else:
            print(cmd, "is not a valid command.")

        print("The result is", result, ".\n")

def main():
    showIntro()
    doLoop()
    showOutro()

main()
