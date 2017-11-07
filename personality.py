## Lab #8
## Author: David Siegel



# emotional state supported by this AI
angry     = 0
disgusted = 1
fearful   = 2
happy     = 3
sad       = 4
surprised = 5

# kinds of interaction from which the user may choose
actions = [ "reward", "punish", "joke", "threaten", "quit" ]
reward   = 0
punish   = 1
joke     = 2
threaten = 3
quit     = 4

# responses that this AI may have when feeling each emotion
responses = [
        "Stop it! You're making me angry!"
    ,   "Ugh! Why don't you just go away?"
    ,   "No, please... don't!"
    ,   "I feel so happy right now!"
    ,   "You're really bringing me down."
    ,   "Oh my goodness, how unexpected!"
    ]

# personality matrix
personality = [
        # reward  punish  joke   threaten
        [ happy,     sad,   disgusted, angry ] # angry
    ,   [ angry,     angry, disgusted, fearful ] # disgusted
    ,   [ surprised, sad,   surprised, fearful ] # fearful
    ,   [ happy,     sad,   happy,     surprised ] # happy
    ,   [ surprised, sad,   happy,     angry ] # sad
    ,   [ happy,     sad,   happy,     fearful ] # surprised
    ]

def main():
    intro()
    primaryLoop()
    ending()

def intro():
    print("Hello! My name is Alice Ingall.")
    print("I am programmed to respond to four different actions:"
          " reward, punish, joke, or threaten.")
    print("To interact with me, enter one of these actions at the prompt.\n")

def ending():
    print("Goodbye.")

def primaryLoop():
    currentEmotion = happy
    while True:
        showEmotion(currentEmotion)
        userAction = getNextInteraction()
        currentEmotion = lookupNewEmotion(currentEmotion, userAction)

def getNextInteraction():
    choice = input("interact> ").strip().lower()
    if choice == "reward":
        return 0
    elif choice == "punish":
        return 1
    elif choice == "joke":
        return 2
    elif choice == "threaten":
        return 3

def lookupNewEmotion(emotion, action):
    return personality[emotion][action]

def showEmotion(emotion):
    print(responses[emotion])

main()

