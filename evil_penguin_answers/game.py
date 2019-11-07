import random
from visuals import stages, game_over, you_win
from utils import load_words, print_output_decorator


class Game:
    """
    This class represents a game of Evil Penguin! Complete the methods in this
    class to complete your own version of the game!
    """

    def __init__(
        self, file_name="scrabble_dictionary.txt", no_cheating=False, unlimited=False
    ):
        """Constructor for a game of hangman.

        Arguments:
            file_name {string} -- name of file containing list of words to use
        """
        self.dictionary_file_name = file_name
        self.no_cheating = no_cheating
        self.unlimited = unlimited

    # The `@staticmethod` decorator makes methods static. This means that this
    # function does not use attributes stored in class instances and thus does
    # not need `self` as the first argument. These methods can be directly called
    # from the class without instantiating an object (e.g.
    # `Game.is_valid_guess('A')`).
    @staticmethod
    def is_valid_guess(string):
        """Determines if input string is valid hangman guess. To be valid, the
        string must have a length of 1 and contain an alphabetic character.
        
        Arguments:
            string {string} -- string containing letter guessed by player
        
        Returns:
            boolean -- True if string is a valid hangman guess, False otherwise
        """
        return len(string) == 1 and string.isalpha()

    @staticmethod
    def get_indices(word, char):
        """Generates a tuple containing the indices where `char` is in `word`.

        This function should be called in `createWordsBukets`.
        
        Arguments:
            word {string} -- the word
            char {string} -- a string containing an alphabetic character
        
        Returns:
            tuple -- tuple containing the indices where char is in word
        """
        indices = []
        for i, c in enumerate(word):
            if c == char:
                indices.append(i)
        return tuple(indices)

    @staticmethod
    def create_words_buckets(words, guess):
        """Given a guessed letter, divide words into buckets based off positions of
        guess in each word. Words that contain the guessed letter in the same
        indices should be sorted into the same bucket. The buckets should be
        returned as a dictionary where the key is a tuple containing the indices
        (ascending order) that the guessed letter appears in the words in the
        bucket, and the value is a set of words belonging to that bucket.

        Example: `Game.create_words_buckets(['ABC', 'BCA', 'ACB', 'ABA'], 'A')`
        should return
        `
        {
            ()    : set(['BCA'])
            (0,)  : set(['ABC', 'ACB']),
            (0, 2): set(['ABA']),
        }
        `

        This function should use `get_indices`.

        This function is called in `get_new_words_set` to assign words into
        equivalence classes based on where the guessed letter appears in the words.
        Words in the same bucket/equivalence class will have the same 'hint'
        (e.g. "**LL*") in hangman.
        
        Arguments:
            words {set[string]} -- set of words
            guess {string} -- guessed letter
        
        Returns:
            dict[tuple[int], set[string]] -- dictionary containing word buckets
        """
        buckets = dict()
        for word in words:
            key = Game.get_indices(word, guess)
            if not key in buckets:
                buckets[key] = set()
            buckets[key].add(word)
        return buckets

    @staticmethod
    def get_new_words_set(words, guess):
        """Given a set of words and a new guess, this function should return the
        largest possible subset of `words` set such that all words in the new
        set contain the guessed letter at the same indices. This should also return
        a tuple containing the indices (ascending) where the guessed letter appears
        in the words in the new set.

        tl;dr using the output of `create_words_buckets`, get the largest bucket and
        its key

        This function is called to update the set of possible 'correct' hangman
        words after a player guesses a letter. It essentially wants to narrow down
        this set of 'correct' words as little as possible so that it has as much
        room as possible to 'cheat' which also remaining consistent with what the
        game has told the player so far about their guesses.
        
        Arguments:
            words {set[string]} -- set of words
            guess {string} -- guessed letter
        
        Returns:
            tuple[int] -- tuple of indices where guess is located in new word set
            set[string] -- new set of words
        """
        buckets = Game.create_words_buckets(words, guess)

        biggest_set = set()
        key_of_biggest_set = tuple()
        for key, val in buckets.items():
            if len(val) > len(biggest_set):
                biggest_set = val
                key_of_biggest_set = key
        return key_of_biggest_set, biggest_set

    @staticmethod
    def get_new_discovered_letters(discovered_letters, indices, guess):
        """Update `discovered_letters` by replacing the specified indices
        in `discovered_letters` with the guessed letter.

        This function is called to update the hangman hint string if the player
        guesses a 'correct' letter.
        
        Arguments:
            discovered_letters {list[string]} -- list of discovered letters in game
            indices {tuple[int]} -- indices of discovered_letters to replace
            guess {string} -- guessed letter to update discovered_letters with
        
        Returns:
            list[string] -- an updated list of discovered letters
        """
        result = discovered_letters
        for i in indices:
            result[i] = guess
        return result

    @staticmethod
    @print_output_decorator
    def get_robot_ascii(num_incorrect_guesses):
        """Given the number of incorrect guesses, returns the appropriate robot ascii.
        If `num_incorrect_guesses` > 6, the returned ascii art remains the same as
        when `num_incorrect_guesses` is 6.

        This method should use `stages`.
        
        `stages` is an imported list of strings that contains the ascii art of
        the evil robot. The indexes in this list correspond to the ascii art given
        `num_incorrect_guesses`. For example, `stages[3]` will be the correct
        ascii art for when the player has guessed incorrectly 3 times.

        Arguments:
            num_incorrect_guesses {int} -- number of incorrect guesses from game
        
        Returns:
            string -- robot ascii art corresponding to `num_incorrect_guesses`
        """
        if num_incorrect_guesses < 0:
            return "invalid number of incorrect guesses"
        elif num_incorrect_guesses < 7:
            return stages[num_incorrect_guesses]
        else:
            return stages[6]

    # Don't touch this method
    def play(self):
        """
        This function contains the main game loop and setup. You don't need to edit
        this.
        """

        if self.no_cheating:
            print("Playing without cheating!")
        if self.unlimited:
            print("Playing with unlimited guesses!")

        # Setting up new game
        words = None
        word_length = random.randint(4, 12)
        if self.no_cheating:
            correct_word = random.choice(
                tuple(load_words(self.dictionary_file_name, word_length))
            )
            words = set([correct_word])
        else:
            words = load_words(self.dictionary_file_name, word_length)

        discovered_letters = ["*" for i in range(word_length)]
        guessed_letters = set([])
        num_guesses = 0
        num_incorrect_guesses = 0

        Game.get_robot_ascii(num_incorrect_guesses)

        # Main game loop
        while True:
            print("\nGuessed letters: " + str(sorted(list(guessed_letters))))
            print(f'\nHint: {"".join(discovered_letters)}\n')

            guess = ""
            while not Game.is_valid_guess(guess):
                guess = input("What letter would you like to guess? ").upper()
            if guess in guessed_letters:
                continue
            guessed_letters.add(guess)
            num_guesses += 1

            guess_indices, words = Game.get_new_words_set(words, guess)

            if len(guess_indices) == 0:
                print("\nYou guessed wrongly!")
                num_incorrect_guesses += 1
            else:
                print("\nGood guess!")
                discovered_letters = Game.get_new_discovered_letters(
                    discovered_letters, guess_indices, guess
                )

            Game.get_robot_ascii(num_incorrect_guesses)

            if num_incorrect_guesses == 6:
                print(game_over)
                if self.unlimited:
                    print(f"Too bad! Don't worry, you can still keep guessing!\n")
                else:
                    print(f"\nThe correct word was {list(words)[0]}!\n")
                    break
            if "*" not in "".join(discovered_letters):
                if num_incorrect_guesses < 6:
                    print(you_win)
                print(f'\nThe correct word was {"".join(discovered_letters)}!\n')
                print(f"\nYou only took {num_guesses} guesses!\n")
                break
