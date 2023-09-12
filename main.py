import random
from hangman_art import logo, stages
from easyword_list import word_list1
from hardword_list import word_list2

print(logo)

difficulty = input("Choose difficulty level between Easy & Hard:\n ").lower()

if difficulty == "Easy":
    word_list = word_list1
elif difficulty == "Hard":
    word_list = word_list2
else:
    print("You typed an invalid choice. It is chosen Easy level as default.")
    word_list = word_list1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo

print(logo)


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")


    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:

        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")


    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("You win.")


    from hangman_art import stages

    print(stages[lives])
