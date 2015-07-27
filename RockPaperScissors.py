# Rock Paper Scissors in Python
from random import randint

def rock_paper_scissors():

    print "Let's play Rock Paper Scissors!"
    playing = True
    user_score = 0
    comp_score = 0
    ties = 0

    while playing == True:
        move = get_input()
        if move == "rock":
            print "You played rock"
            play = "y"
        elif move == "paper":
            print "You played paper"
            play = "y"
        elif move == "scissors":
            print "You played scissors"
            play = "y"
        elif move == "quit":
            print "Quitting game, Goodbye"
            playing = False
            play = "n"
        else:
            print "Command not recognized, try again"
            play = "n"

        if play == "y":
            comp_move = get_comp_move()
            print "The computer played %s" % comp_move
            result = check_hand(move, comp_move)
            if result == "t":
                print "Tie Game!"
                ties += 1
            elif result == "w":
                print "You win!"
                user_score += 1
            elif result == "l":
                print "You lose :("
                comp_score += 1

        print "You: %d, Computer: %d, Ties: %d\n" %(user_score, comp_score, ties)

# Grabs input from the user
def get_input():
    txt = input("Please enter 'rock', 'paper', 'scissors', or 'quit'")
    txt.lower()
    return txt

# Generates random move from the computer
def get_comp_move():
    num = randint(1, 3)
    if num == 1:
        move = "rock"
    elif num == 2:
        move = "paper"
    else:
        move = "scissors"
    return move

# Checks hands, returns w, l or t
def check_hand(you, comp):
    if you == comp:
        return "t"
    elif (you == "rock" and comp == "scissors") or (you == "paper" and comp == "rock") or (you == "scissors" and comp == "paper"):
        return "w"
    elif (you == "rock" and comp == "paper") or (you == "paper" and comp == "scissors") or (you == "scissors" and comp == "rock"):
        return "l"


rock_paper_scissors()
