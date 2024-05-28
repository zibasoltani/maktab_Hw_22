import random
import requests
import time

# API endpoint for random word
WORD_API = "https://api.com.ninjas/v1/randomword?language=en"

# Predefined categories and words
CATEGORIES = {
    "animals": ["dog", "cat"],
    "colours": ["red", "blue"],
    "topic_names": ["Colours", "Animals"],
    "topics": {'Colours': "colours", 'Animals': "animals"}
}


def get_random_word():
    try:
        response = requests.get(WORD_API)
        if response.status_code == 200:
            return response.json()['word']
    except Exception as e:
        print(f"An error occurred while fetching the word: {e}")

    # Fallback to predefined words if API fails
    category = random.choice(list(CATEGORIES.keys()))
    word = random.choice(CATEGORIES[category])
    return word


def play_hangman():
    word = get_random_word()
    word_masked = ["_" for _ in word]
    attempts = 3 * len(word)
    time_limit = 60  # Time limit in seconds
    start_time = time.time()
    guessed_letters = set()

    print("Welcome to Hangman!")
    print(" ".join(word_masked))

    while attempts > 0 and time.time() - start_time < time_limit:
        if time.time() - start_time > time_limit / 2:
            print(f"Time remaining: {time_limit - int(time.time() - start_time)} seconds")

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
            for i in range(len(word)):
                if word[i] == guess:
                    word_masked[i] = guess
        else:
            print("Incorrect!")
            attempts -= 1

        print(" ".join(word_masked))

        if "_" not in word_masked:
            print("Congratulations! You won!")
            break

    if "_" in word_masked:
        print(f"Game over! The word was: {word}")
    else:
        print(f"Game ended in {int(time.time() - start_time)} seconds")


if __name__ == "__main__":
    play_hangman()
