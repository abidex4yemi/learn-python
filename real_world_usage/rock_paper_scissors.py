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


def save_results(w, t, l):
    try:
        text_file = open("history.txt", "w")
        text_file.write(w + "," + t + "l")
        text_file.close()
    except FileNotFoundError:
        print(f"{FileNotFoundError}")


# Welcome message
results = load_results()
wins = 0
ties = 0
losses = 0

print("Welcome to rock, scissors, paper")
print("Wins: %d, Ties: %d, Losses: %d" % (wins, ties, losses))
print("Please choose one of the choices below to continue...")


# Initialize user and computer choices
computer = random.randint(1, 3)

# Reading user input from commandline
user = input("[1] Rock  [2] Paper  [3] Scissors      [9] Quit\n")

# Game loop
while not user == 9:
    if user == 1:
        if computer == 1:
            print("Computer choose rock...tie!")
