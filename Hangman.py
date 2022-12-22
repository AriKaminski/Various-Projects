import random
words = ["Hurts", "Goedert", 'Van', 'Poggers' , 'Sanders', 'Brown', 'White', 'Eagles', 'Scooter', 'Mongoose', 'Extreme', 'Birds']
secretWord = random.choice(words)
secretWord = secretWord.lower()
lettersGuessed = ""

Lives = 6

while Lives > 0:
    
    guess = input("Enter your letter: ")
    guess = guess.lower()

    if guess in secretWord:
        print(f"Correct! There is one or more {guess} in the secret word.")
        
    else:
        Lives -= 1
        print(f"Incorrect! You have {Lives} remaining.")

    lettersGuessed = lettersGuessed + guess
    wrongLetterCount = 0

    for letter in secretWord:
        if letter in lettersGuessed:
            print(f"{letter}", end="")
        else:
            print('_', end = "")
            wrongLetterCount += 1
    print("")

    if wrongLetterCount == 0:
        print(f"Congratulations! The secret word was: {secretWord}.")
        break
    if Lives == 0:
        print(f"You lost! The secret word was {secretWord}")

