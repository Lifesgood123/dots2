def break_words(stuff):
    """
this Function uses the slipt method to seterate strings of multiple words into arrays
    """
    words = stuff.split(' ')
    return words

def sort_words(words) :
    """
this Function calls a sort() in order to sort words
    """
    return sorted(words)

def print_first_word(words):
    """
Pretty self explainatory, but this gets and array of words and returns
the word with an index of zero
    """
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """
See above
    """
    print(words.pop(-1))
def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_last_and_first_sorted(sentence):
    words = sort_sentence(sentence)
    print_last_word(words)
    print_first_word(words)
