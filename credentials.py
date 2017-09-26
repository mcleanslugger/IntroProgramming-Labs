# credentials.py
# David Siegel
# CMPT 120L 113

FullName = ""
name = ""
username = ""
password = ""

def getName():
    global FullName, name
    firstName = input("Please enter your first name: ").lower()
    lastName = input("Please enter your last name: ").lower()
    name = [firstName, lastName]
    FullName = " ".join(name)

def CreateUsername(giveName):
    global username
    username = ".".join(giveName)
    username = username + "@marist.edu"

def CreatePassword():
    global password
    password = input("Create a new password: ")
    
def checkStrength(Password):
    if len(Password) >= 8:
        if (Password.lower() == Password or Password.upper() == Password):
            return False
        else:
            return True
    else:
        return False

def main():
    global name, password, username
    getName()
    CreateUsername(name)
    CreatePassword()
    checkStrength(password)
    while (checkStrength(password) == False):
        print("Sorry that's not strong enough. Try again.")
        CreatePassword()
    print("Congratulations! Your new username is", username)

main()
