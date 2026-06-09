import random

def play_hangman():
    words = ['python', 'coding', 'internship', 'developer', 'computer']
    word = random.choice(words)
    guessed = "_" * len(word)
    attempts = 6
    guessed_letters = []

    print("--- Welcome to Hangman Game ---")
    
    while attempts > 0 and "_" in guessed:
        print(f"\nWord: {guessed}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            guessed = "".join([char if char in guessed_letters else "_" for char in word])
            print("Good guess!")
        else:
            attempts -= 1
            guessed_letters.append(guess)
            print("Wrong guess!")
            
    if "_" not in guessed:
        print(f"\nCongratulations! You won! The word was: {word}")
    else:
        print(f"\nGame Over! The word was: {word}")

if __name__ == "__main__":
    play_hangman()
  
