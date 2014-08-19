import numpy as np

# Aleksey Orekhov
#Routines used to find anagrams given a filename and list of target words

#Rewriting the routine to find multiple anagrams with the help of currying slowed the executions from 1.4 to 6.5 seconds
#I suspect packing and unpacking to be responsible for most of the hit to performance.
#However, the time does not significantly change if you look for 1 word or 10 words with the new code (less than 1
#second difference)

def build_anagram_finder(target_word):
    """
    Returns a function that checks for anagrams to the given word
    :param str target_word: word that we want to check against input for anagrams
    """
    target_len = len(target_word)
    target_sorted = sorted(target_word)

    def anagram_finder(letter_list):
        """
        :param list[str]
        """
        if len(letter_list) != target_len:
            return False
        if (all((x == y) for (x, y) in zip(target_sorted, letter_list))):
            return True
        else:
            return False

    return anagram_finder


def look_for_anagrams(filename, target_words):
    """
    Finds anagrams to the words in target_words in file filename. All the words are sorted and then we look for matches.
    Faster methods are possible, but time constraints don't allow implementation unless needed.

    :param str filename: filename to look for words in
    :param list[str] target_words: list of words we are interested in
    :return dict[str,list[str]]: dictionary mapping from target words to lists of found anagrams
    """
    anagrams = {}  #initialize dictionary that accepts outputs. defaultdict was not useful when no matches found
    for target_word in target_words:
        anagrams[target_word] = []
    with open(filename) as word_file:
        cleaned_target_words = [x.strip().casefold() for x in target_words]
        anagram_finders = [build_anagram_finder(x) for x in
                           cleaned_target_words]  #build anagram finder functions for each word
        for word in word_file:
            word_cleaned = word.strip().casefold()
            sorted_letter_list = sorted(word_cleaned)
            is_anagram_list = np.array([x(sorted_letter_list) for x in anagram_finders])
            true_indexes = np.where(is_anagram_list == True)[0]
            for index in true_indexes:
                try:
                    anagrams[cleaned_target_words[index]].append(word_cleaned)
                except TypeError:  #no anagrams found, empty list
                    pass
    return anagrams

