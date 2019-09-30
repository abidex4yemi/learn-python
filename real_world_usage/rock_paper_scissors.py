import random

# file i/o functions for historical result


def load_results():
    try:
        text_file = open("history.txt", "r")
        history = text_file.read().split(",")
        print(history)
        text_file.close()

        return history
    except FileNotFoundError:
        print(f"{FileNotFoundError}")


def save_results(wins, ties, losses):
    try:
        text_file = open("history.txt", "w")
        text_file.write(f"Wins: {wins}, Ties: {ties}, Losses: {losses}")
        text_file.close()
    except FileNotFoundError:
        print(f"{FileNotFoundError}")


# initialize statistics
wins = 0
ties = 0
losses = 0

# Welcome message
print("Welcome to rock, scissors, paper")
print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))
print("Please choose one of the choices below to continue...")


# Initialize user and computer choices
computer = random.randint(1, 3)

# Reading user input from commandline
user = int(input("[1] Rock  [2] Paper  [3] Scissors      [9] Quit\n"))

# Game loop
while not user == 9:
    # user chooses rock
    if user == 1:
        if computer == 1:
            print("Computer chose rock...tie!")
            ties += 1
        elif computer == 2:
            print("Computer chose paper...computer wins :)")
            losses += 1
        else:
            print("Computer chose scissors...you wins ):")
            wins += 1

    # user chooses paper
    elif user == 2:
        if computer == 1:
            print("Computer chose rock...you win ):")
            wins += 1
        elif computer == 2:
            print("Computer chose paper...tie!")
            ties += 1
        else:
            print("Computer chose scissors...you win ):")
            losses += 1

    # user chooses scissors
    elif user == 3:
        if computer == 1:
            print("Computer chose rock...computer wins :)")
            losses += 1
        elif computer == 2:
            print("Computer chose paper...you win ):")
            wins += 1
        else:
            print("Computer chose scissors...tie!")
            ties += 1

    # print updated statistics
    print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))

    # S
    # Note: if another input() is not provided at the #
    # end this will result in infinite loop           #
    ###################################################

    # Prompt user to make another selection
    print("Please choose to continue ):")
    computer = random.randint(1, 3)
    user = int(input("[1] Rock  [2] Paper  [3] Scissors      [9] Quit\n"))

# Outside will loop game over
# Print game statistics
save_results(wins, ties, losses)
load_results()
