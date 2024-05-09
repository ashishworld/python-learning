print("To quit the GAME enter 0")
num = 50
guess = 0
attempt = 0

while True:
    guess = int(input("Guess a number: "))
    if guess == 0:
        print("you loose the game")
        break

    attempt += 1

    if guess == num:
        print(f"You Guessed it right! {attempt} attempts")
        break
