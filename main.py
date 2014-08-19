import argparse
from time import time
from datetime import timedelta

import AnagramFinder



# Aleksey Orekhov
# Command Line Interface for AnagramFinder

###Parse Arguments###
parser = argparse.ArgumentParser(description='Find anagrams to target words')
parser.add_argument('words', metavar='word', type=str, nargs='+',
                    help='word that the script will find anagrams to')
parser.add_argument('-f', metavar='filename', type=str, default="words.txt",
                    help='File to look in for anagrams')
args = parser.parse_args()



###Main Routine###
start = time()  #time routine
anagrams_dict = AnagramFinder.look_for_anagrams(filename=args.f, target_words=args.words)
fin = time()
duration = fin - start

###Print Anagrams Found
for (k, v) in anagrams_dict.items():
    print("{}: {}".format(k, " ".join(v)))

print("Time Taken (H:M:S): {0}".format(timedelta(seconds=duration)))

