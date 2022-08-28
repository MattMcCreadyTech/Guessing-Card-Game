guess_count = 0
secret_card = 'spade'
max_guess = 3
while guess_count < max_guess:
    guess = input("""Guess the suit of the card: 
>Heart
>Spade
>Club
>Diamond
-""")
    guess_count += 1
    if guess.lower() == secret_card:
        print('Congrats, you win!')
        break
    elif guess != secret_card:
        print('Sorry, try again. ')
        if guess_count < max_guess:
            continue
        print("Sorry, you're all out of guesses!! :( ")
