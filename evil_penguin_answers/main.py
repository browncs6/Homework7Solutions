import sys
import argparse
from game import Game

"""
Use argparse to parse the following arguments from the command line:
    --dictionary : follow this with a path (string) to text file with words
    --no_cheating : disables cheating in the game (by the computer) if included
    --unlimited : allows unlimited guesses in the game if included

You can find documentation on argparse here:
https://docs.python.org/3.7/library/argparse.html

You can find documentation on adding custom arguments here:
https://docs.python.org/3.7/library/argparse.html#the-add-argument-method
"""

if __name__ == "__main__":
    # Put your argparse code here!
    parser = argparse.ArgumentParser(description="Play the game Evil Penguin")
    parser.add_argument(
        "--dictionary",
        dest="file_name",
        type=str,
        default="scrabble_dictionary.txt",
        help="file name/path to text file of words to use for game",
    )
    parser.add_argument(
        "--no_cheating",
        dest="no_cheating",
        action="store_true",
        default=False,
        help="prevent cheating in Evil Penguin",
    )
    parser.add_argument(
        "--unlimited",
        dest="unlimited",
        action="store_true",
        default=False,
        help="play with unlimited guesses",
    )

    # Create a new game instance from the imported Game class and call the `play`
    # method to play!
    args = parser.parse_args()
    g = Game(args.file_name, args.no_cheating, args.unlimited)
    g.play()
