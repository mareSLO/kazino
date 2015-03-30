from random import randint
secret = randint(0, 15)
print("Welcome to Casino Mond!")
guess = 0
while guess != secret:
    g = raw_input("Guess the hidden number: ")
    guess = int(g)
    if guess == secret:
        print("You hit the Jackpot brother!")
    else:
        if guess > secret:
            print("You aimed too high, guess again")
        else:
            print("You aimed too low, guess again")
print("Now you can finally afford that Ferrari!")
