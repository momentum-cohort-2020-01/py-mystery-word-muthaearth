import random


class Game:
    def __init__(self, player_name):
        self.word = "Shun"
        self.player = Player()
        self.max_attempts = 8
        self.start_game()
        self.playing = True
        self.level = {'novice': 0, 'expert': 1000}

        def __str__(self):
            return "nCrypt dCrypt Shun"

    # def get_words(self):
    #     with open('words.txt') as f:
    #         words = []
    #         pos = {}
    #         position = itertools.count()
    #         for line in f:
    #             for word in line.split():
    #                 if word not in pos:
    #                     pos[word] = position.next()
    #                     words.append(word)
    #     return sorted(words, key=pos.__getitem__)

    def get_words(self):
        with open('words.txt', 'r') as f:
            words = f.readlines()
        """ file opened in read mode as string """
        """ return list of all lines of file data """
        """render words in uppercase and remove leading and trailing characters from copy of string"""
        words = [word.strip().upper() for word in words]
        return words

    # def strip_cap(self):
    #     words = [word.strip().upper() for word in words]

    def select_word(self):
        words = self.get_words()
        word = random.choice(words)
        novice, expert = self.level['novice'], self.level['expert']
        """ as long as selected word length for novice is less than or equal to selected word length for expert, pass a word into word"""
        while not (novice <= len(word) <= expert):
            word = random.choices(words)
        self.word = word

        # i = 0
        # j = 0
        # while True:
        #     if i == len(word_list):
        #         i = 0
        #         j += 1
        #     elif thing_I_want(word_list[i], word_list2[j]):
        #         do_something()
        #         break
        #     else:
        #         i += 1

    def set_level(self):
        series_levels = {
            'beginner': {'novice': 4, 'intermediate': 7, 'expert': 10},
            'intermediate': {'novice': 6, 'intermediate': 9, 'expert': 12},
            'advanced': {'novice': 8, 'intermediate': 11, 'expert': 14},

        }
        print("Beginner: nCrypted word with 4-8 letters")
        print("Intermediate: nCrypted word with 7-11 letters")
        print("Advanced: nCrypted word with 10-14 letters")

        level = input(
            "Select Beginner, Intermediate, or Advanced: ").lower().strip()
        self.level = series_levels[level]

    def display_status(self):
        """if letter selected by player is correct, store character in list and print concatenated letters"""
        log_attempts = self.player.attempts['right']
        """ if wrong, leave an underscored space for the character"""
        dCrypt_list = [
            char if char in log_attempts else '_' for char in self.word]
        print()
        print(''.join(dCrypt_list))

    def start_game(self):
        print("Welcome to nCrypt dCrypt Shun (pronounced, 'shoon')")
        print('The season for unlocking your neural senses')
        print('Good Luck!')
        self.set_level()
        self.select_word()

        print(
            f'\nThe word contains {len(self.word)} letters. Begin your dCrypt Shun!\n')

        print(" " * len(self.word))

    def challenge(self):
        self.challenge()

       # self.total_attempts()
        while self.playing:
            decrement = len(self.player.attempts["wrong"])
            print('\n'+'='*42)
            print(
                f'\n*** dCryptor, you have {self.max_attempts-decrement} remaining attempts ***\n')
            attempt = self.player.attempt()
            if attempt in self.word:
                print('dCrypt Shun おめでとう (Omedetō)')
                print('\n *** Congratulations! ***\n')
                self.player.attempts['right'].append(attempt)

            else:
                print('\n nCrypt Shun! 再試行(Sai shikō)\n')
                print('\n *** Retry! ***\n')
                self.player.attempts['wrong'].append(attempt)

        self.display_status()

        log_attempts = self.player.attempts['right']

        """player wins game if concatenated chars in total_attempts matches characters in selected word"""
        total_attempts = ''.join(
            [char for char in self.word if char in log_attempts])

        if self.challenge == self.word:
            self.player.win = True
            self.playing = False

        # """player chances done"""
        elif len(self.player.attempts['wrong']) == self.max_attempts:
            self.playing = False
            print('\n'+'='*42)
            print("\n nCrypt Shun! 残念な (Zan 'nen' na)\n")
            print('\n *** Too bad! ***\n')

        self.finish_game()

        def finish_game(self):
            if self.player.win:
                print('\nf${self.name}, nCrypt Shun! あなたが勝った (Anata ga katta)\n')
                print('\n *** You Won! ***\n')

            else:
                print(
                    '\nf${self.name}, nCrypt Shun! あなたが負けた (Anata ga maketa)\n')
                print('\n *** You Lost! ***\n')

        print(f'*** nCrypt Shun was: {self.word} ***')

        sleep(1)

        new_game = input('\n\n dCrypt again? (y) or (no): ')
        while not (new_game == 'y' or new_game == 'n'):
            new_game = input('dCrypt again? (y) or (n): ')
            if new_game == 'n':
                exit()
            elif new_game == 'y':
                print('\n *** Begin nCrypt dCrypt Shun! ***\n')


class Player:
    def __init__(self):
        self.attempts = {'right': [], 'wrong': []}
        self.win = False

    def str(self):
        return "*** Embrace your season for Winning! ***"

    def all_attempts(self):
        return self.attempts['right'] + self.attempts['wrong']

    def attempt(self):
        entry = False
        while not entry:
            attempt = input('What letter to dCrypt: ').upper()
            if not attempt.isalpha() or len(attempt) != 1:
                print('Enter a letter')
                continue
            elif attempt in self.all_attempts():
                print('Letter already entered. Try again.')
                continue
            else:
                entry = True
                return attempt


def main():
    player_name = input('Enter your name: ')
    Game(player_name).start_game()


if __name__ == '__main__':
    main()
