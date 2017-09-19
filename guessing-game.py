def main():
    animal = "lion"
    while animal == "lion":
        print("The program is thinking of an animal.")
        guess = str.lower(input("Guess the name of the animal: "))
        if guess == animal:
            print("Congratulations! You guessed correctly!")
            animal = ""
        elif guess == "quit":
            return
        else:
            print("Sorry, that's not correct. Please try again.")

main()
