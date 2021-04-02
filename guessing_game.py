import random
def start_game():
    print("You are now playing JJ's Guessing Game!")
    solution = random.randrange(11)
    guess_attempts = 1
    while True:
        try:
            guess = int(input("Pick a number betweeen 1 - 10: "))
            if guess < 1 or guess > 10:
                raise ValueError
        except ValueError:
            print("You must enter an integer between 1-10. Try again!")
        else:
            if guess > solution:
                print("It's lower")
                guess_attempts += 1
            elif guess < solution:
                print("It's higher")
                guess_attempts += 1
            elif guess == solution:
                print("Got it! It took you {} attempts to guess the correct number.".format(guess_attempts))
                break
    print("Thanks for playing JJ's Guessing Game!")        
start_game()