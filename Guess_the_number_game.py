import random

def NumberGuessGame():
    number = random.randint(1, 10)
    for i in range(0, 3):
        user = int(input("Guess The Number from 1-10: "))
        if user == number:
            print("Hurray!!")
            print(f"You guessed the number right its {number}")
            break
        elif user > number:
            print("Your guess is too high")
        elif user < number:
            print("Your guess is too low")
    else:
        print(f"Nice Tryy! , but the number is {number}")

