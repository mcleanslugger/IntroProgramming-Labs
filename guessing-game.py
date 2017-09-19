def main():
    animal = "lion"
    while animal == "lion":
        print("The program is thinking of an animal.")
        guess = str.lower(input("Guess the name of the animal: "))
        if guess == animal:
            like = str.lower(input("Congratulations! You guessed correctly!\nDo you like that animial? (y/n)"))
            if like == "y":
                print("I like that animal too!")
            else:
                print("Too bad.")
            animal = ""
        elif guess[0] == "q":
            return
        else:
            print("Sorry, that's not correct. Please try again.")

main()
