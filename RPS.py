import random
def Rock_Paper_Scissors() :
    choices = ["Rock", "Paper", "Scissors"]
    print("Welcome to Rock, Paper, Scissors️")
    print()

    def player_choice():
        game = True
        while (game):
            ply = int(input("Enter the number \n 0 -> Rock, \n 1 -> Paper, \n 2 -> Scissors️"))
            if (ply > -1 and ply < 3):
                game = False
            else:
                print("Wrong Choice Man!")
        return (choices[ply])

    def computer_choice():
        comp = random.choice(choices)
        return comp

    def winner(x, y):
        if (x == y):
            print("It's a tie!")
        elif (x == "Rock"):
            if (y == "Paper"):
                print("Computer Won!")
            else:
                print("Player Won!")
        elif (x == "Paper"):
            if (y == "Scissors"):
                print("Computer Won!")
            else:
                print("Player Won!")
        elif (x == "Scissors"):
            if (y == "Rock"):
                print("Computer Won!")
            else:
                print("Player Won!")

    player = player_choice()
    computer = computer_choice()
    print("player = {}".format(player))
    print("computer = {}".format(computer))
    winner(player, computer)
