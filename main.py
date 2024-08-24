from GenerateGameData import GenerateGameData


def generate_lower_bound():
    while True:
        try:
            lower = int(input("Please enter lower bound: "))
            return lower
        except ValueError:
            print("Please enter a number")


def generate_upper_bound(lower):
    while True:
        try:
            upper = int(input("Please enter upper bound: "))
            while upper <= lower:
                upper = int(input("Please enter higher upper bound: "))
            else:
                pass
            return upper
        except ValueError:
            print("Please enter a number")


def play_game(number_to_guess, minimum_guesses):
    guesses = minimum_guesses
    while guesses > 0:
        try:
            print(f"You have {guesses} times to guess ")
            guess = int(input("Please enter your guess: "))
            guesses -= 1
            if guess > number_to_guess:
                print("Try Again! You guessed too high")
            elif guess < number_to_guess:
                print("Try Again! You guessed too small")
            elif guess == number_to_guess:
                print("Congratulations!")
                break
        except ValueError:
            print("Please enter a number")
    else:
        print("Better Luck Next Time!")


lower_bound = generate_lower_bound()
upper_bound = generate_upper_bound(lower_bound)

print(f"Lower bound is {lower_bound}")
print(f"Upper bound is {upper_bound}")

data = GenerateGameData(lower_bound, upper_bound)

minimum_guesses = data.generate_minimum_guess()

number_to_guess = data.number_to_guess()

print(number_to_guess)

play_game(number_to_guess, minimum_guesses)



