# Define the word to guess
word_to_guess = "EVAPORATE"

# Initialize a set to keep track of guessed letters
guessed_letters = set()

# Create a list to store the current state of the word with underscores
current_word_state = ["_"] * len(word_to_guess)

print("Welcome to Hangman!", " ".join(current_word_state))

# Main game loop
while "_" in current_word_state:
    guess = input("Guess your letter: ").upper()

    # Check if the guess is a single letter
    if len(guess) == 1 and guess.isalpha():
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word_to_guess:
            guessed_letters.add(guess)
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    current_word_state[i] = guess
            print(" ".join(current_word_state))
        else:
            guessed_letters.add(guess)
            print(f"{guess} is Incorrect!")
    else:
        print("Please enter a valid single letter guess.")

# Game over message
print("Congratulations! You guessed the word:", word_to_guess)
