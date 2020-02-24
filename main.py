import random
import sys


Gallow printouts
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
        self.player = Player(input("Welcome to Hangman. What is your name? "))
        self.game_list = open("words.txt", "r")
        self.generate_list()
        self.play_game()

    def generate_list(self):
        self.game_list = self.game_list.read().split('\n')

    def pick_diff(self, player, choice):
        print("\nHello, " + self.player.name +
              "Pick a level of difficulty. Novice - 8 letter words\n  Intermediate - 10 letter words\n  Expert - 15+ letter words\n>")
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
        words = []

        for word in self.game_list:

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

    def random_word_list(self, level_choice):
        list = self.word_length(level_choice)
        random_word = random.choice(list)
        return random_word.upper()

    # def transform_random_list(self, word):
    #     return list(word)

    def start_over(self):
        repeat = input('Would you like to play again? [Y/N]\n >').lower()
        if repeat == "yes" or repeat == "y":
            self.player.guesses = 8
            self.start_over()

        else:
            print("Thanks for playing! Have a great day!")
            sys.exit()

    def play_game(self, game_list):
        blanks = list("_" * len(self.game_list))
        guessed = []
        incorrect = 8

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
                            # word_guess = "".join(blanks)
                            return blanks
                        if blanks == word:
                            print(
                                "\n\nCONGRATULATIONS, YOU WON!!\nYour word was " + ''.join(word) + ".\n")
                            self.start_over()
                            break

                elif letter not in word:
                    incorrect -= 1
                    guessed.append(letter)
                    print("\n\n!Only single letters allowed!\n\n")

            else:
                print(gallows[0])
                print("\nSorry, your game is over!\nYour word was " +
                      ''.join(word) + ".")
                self.start_over()
                break


class Player:
    def __init__(self, name):
        self.name = nameAnn

    def __str__(self):
        return f"{self.name}"


game = Game()
