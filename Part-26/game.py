num = 50
guess = 0
attempt = 0

while guess != num:
    guess = int(input("Guess a number: "))
    attempt += 1

print(f"You Guessed it right! {attempt} attempts")
