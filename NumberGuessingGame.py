import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number betweeon 1 and {x}: "))
        if guess == (random_number - 5):
            print("So close! Just a little low")
        elif guess == (random_number + 5):
            print("So close! Just a little high")
        elif guess < random_number:
            print("Good try, but it was too low, keep trying!")
        elif guess > random_number:
            print("Good try, but it was too high, keep trying!")

    print("Congrats you guessed the number! Would you like to play again?")
    play_again = input("Play again? ")
    if play_again.__eq__("yes"):
        print("Great! Pick a number to be the max number in the range")
        newX = int(input("Pick a number!: "))
        guess(newX)
    elif play_again.__eq__("no"):
        print("See you next time!")

