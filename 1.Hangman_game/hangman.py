import random

# STEP 1: Create a list of words
words = ["python", "computer", "program", "coding", "developer","codealpha"]


# STEP 2: Select one random word
word = random.choice(words)


# STEP 3: Create an empty list to store the letters guessed by the player
guessed_letters = []


# STEP 4: Set the game variables
incorrect_guesses = 0
max_guesses = 6


# STEP 5: Display the welcome message
print("🎮 Welcome to Hangman!")
print("I have selected a secret word.")
print("Try to guess it one letter at a time.")


# STEP 6: Start the game
while incorrect_guesses < max_guesses:

    # STEP 7: Create an empty string 
    display_word = ""


    # STEP 8: Look at each letter 
    for letter in word:

        # STEP 9: Check whether this letter was guessed
        if letter in guessed_letters:
            display_word += letter + " "

        else:
            display_word += "_ "


    # STEP 10: Show the current word
    print("\nWord:", display_word)


    # STEP 11: Show the letters already guessed
    print("Guessed letters:", " ".join(guessed_letters))


    # STEP 12: Check whether the player has guessed the  word
    if all(letter in guessed_letters for letter in word):

        print("🎉 Congratulations!")
        print("You guessed the word:", word)

        break


    # STEP 13: Ask the player for a letter
    guess = input("Enter a letter: ").lower()


    # STEP 14: Check whether the input is valid
    if len(guess) != 1 or not guess.isalpha():

        print("Please enter only ONE letter.")
        continue


    # STEP 15: Check whether the player already guessed this letter
    if guess in guessed_letters:

        print("You already guessed that letter.")
        continue


    # STEP 16: Add the player's guess to the list
    guessed_letters.append(guess)


    # STEP 17: Check whether the guessed letter exists in the word
    if guess in word:

        print("✅ Correct guess!")

    else:

        incorrect_guesses +=1

        print("❌ Wrong guess!")
        print("Incorrect guesses:", incorrect_guesses)


# STEP 18: If the player used all 6 wrong guesses
if incorrect_guesses == max_guesses:

    print("\n😔 Game Over!")
    print("The secret word was:", word)