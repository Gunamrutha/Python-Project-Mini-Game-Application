import pyfiglet
import Guess_the_number_game
import RPS
import quiz

ascii_banner = pyfiglet.figlet_format("Hello User!")
print(ascii_banner)

def ChooseGame():
    user_choice = int(input("Enter your choice:\n 1 = Guess The Number \n 2 = Quiz  \n 3 =Rock Paper Scissors  \n" ))
    if user_choice == 1:
        Guess_the_number_game.NumberGuessGame()
    elif user_choice == 2:
        quiz.Quiz()
    elif user_choice == 3:
        RPS.Rock_Paper_Scissors()
ChooseGame()
choice = input("Want To Play Again?")
if choice == "Yes" :
    ChooseGame()
elif choice == "No":
    print("See You Soon :)")




