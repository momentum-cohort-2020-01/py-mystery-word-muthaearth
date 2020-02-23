import random
import sys

# Gallow printouts
gallows = ["_______\n|     |\n|     O\n|    -|-\n|     |\n|    / \\ \n|\n=======",
           "_______\n|     |\n|     O\n|    -|-\n|     |\n|    /\n|\n=======",
           "_______\n|     |\n|     O\n|    -|-\n|     |\n|\n|\n=======",
           "_______\n|     |\n|     O\n|    -|\n|     |\n|\n|\n=======",
           "_______\n|     |\n|     O\n|     |\n|     |\n|\n|\n=======",
           "_______\n|     |\n|     O\n|\n|\n|\n|\n=======",
           "_______\n|     |\n|\n|\n|\n|\n|\n=======",
           ]


class Game:
    def __init__(self):
        self.word = "gallows"
        name = input("Welcome to Hangman. What is your name? ")
        print(f"Hello, Let's play!")
        # word_length()
        self.start_game = ()
        self.playing = True
        # new_game = ()

    # def __str__(self):
    #     return "Hangman Gallows"

    def get_words(self):
        with open('words.txt', 'r') as f:
            words = f.readlines()
            words = [word.strip().upper() for word in words]
            return words

    def pick_diff(self, choice):
        """Let the player pick and confirm a difficulty level."""
        prompt = "Pick a level of difficulty. (Easy, Medium, Hard)\n>"
        self.choice = input(
            'Enter the number associated with level of difficulty you wish to play: ')
        print("\t1. Beginner (11 guesses)")
        print("\t2. Intermediate (9 guesses)")
        print("\t3. Expert (7 guesses)")

        if (str(self.choice) == "1"):
            number_of_guesses = 8
            print("\nYou have chosen %s and will receive %d guesses." %
                  ("Beginner", number_of_guesses))

        elif (str(self.choice) == "2"):
            number_of_guesses = 7
            print("\nYou have chosen %s and will receive %d guesses." %
                  ("Intermediate", number_of_guesses))

        elif (str(self.choice) == "3"):
            number_of_guesses = 6
            print("\nYou have chosen %s and will receive %d guesses." %
                  ("Expert", number_of_guesses))

        else:
            print("\nNot a valid entry. Please try again\n")
            self.choice = input(
                'Enter the number associated with level of difficulty you wish to play: ')
            return self.choice

    def change_diff(self, pick_diff):
        pick_diff()
        """Allow the player a chance to change difficulty level."""
        message = "\nYou picked " + pick_diff + \
            ".\nYou get six incorrect guesses before you lose.\nDo you want to change it? [Y/N]\n>"
        answer = ""
        while answer not in ['y', 'n']:
            answer = input(message)
            answer = answer.lower()
        if answer == 'y':
            pick_diff()
        if answer == 'n':
            print("\nHere we go!\n")

    def word_length(self, level_choice):
        words = self.get_words()
        word = random.choice(words)

        for word in words:

            if level_choice == 1 or level_choice == 'Beginner':
                if len(word) >= 5 and len(word) <= 8:
                    words.append(word)

            elif level_choice == 2 or level_choice == 'Intermediate':
                if len(word) >= 9 and len(word) <= 13:
                    words.append(word)

            elif level_choice == 3 or level_choice == 'Expert':
                if len(word) >= 14:
                    words.append(word)
                    return words

    def start_game(self):
        """Run the actual game of hangman."""
        word = list(self.word)
        blanks = list("_" * len(word))
        guessed = []
        incorrect = 7
        while incorrect > 0:
            print("\n" + gallows[incorrect]
                  + "\nYou have {} chances left.".format(incorrect)
                  + "\nYour word: " + "".join(blanks)
                  + "\nGuessed letters: " + ", ".join(guessed)
                  )
            letter = input("Your guess: ").lower()
            if len(letter) == 1 and letter.isalpha():
                if letter in guessed:
                    print("\n\nYou already guessed that!")
                elif letter in word:
                    for index, character in enumerate(word):
                        blanks = list(blanks)
                        if character == letter:
                            blanks[index] = letter
                            # current = "".join(blanks)
                            if blanks == word:
                                print(
                                    "\n\nCONGRATULATIONS, YOU WON!!\nYour word was " + ''.join(word) + ".\n")
                                play_again(self.word)
                elif letter not in word:
                    incorrect -= 1
                    guessed.append(letter)
            else:
                print("\n\n!Only single letters allowed!\n\n")
        else:
            print(gallows[0])
            print("\nSorry " + player +
                  ", your game is over!\nYour word was " + ''.join(word) + ".")

        self.end_game()

    def end_game(self):
        if self.player.win:
            print('\n *** You Won! ***\n')

        else:
            print('\n *** You Lost! ***\n')

    # new_game()

    def new_game(self):
        """ Ofer to play game again"""
        repeat = input('Would you like to play again? [Y/N]\n >').lower()
        if repeat == "yes" or repeat == "y":

            """Welcome the player"""
            player = input(
                "Let's play Hangman! Please type your name.\n>").title()
            print("\nHello, " + player + "!\nWhich difficulty would you like?\n  Novice - Eight letter words\n  Intermediate - Ten letter words\n  Expert - Fifteen+ letter words")

            # Select the difficulty and begin the game
            pick_diff()

        else:
            play_again = False
            print("Thanks for playing! Have a great day!")
            sys.exit()
# loop end


# class Player:
#     def __init__(self):
#         self.attempts = {'right': [], 'wrong': []}
#         self.win = False


if __name__ == '__main__':
    Game()
