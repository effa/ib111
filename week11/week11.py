"""Week 11: Text processing and data analysis.

Assumes the following files in the same directory as this script:
- 'alice-in-wonderland.txt': https://github.com/effa/ib111/week11/alice-in-wonderland.txt
- 'devatero-pohadek.txt': https://github.com/effa/ib111/week11/devatero-pohadek.txt

Edit the last two lines of this script to run either main() or test().
- test() runs provided doctests, shows errors (or nothing if everything works)
- main() runs any manual tests and print results
"""
import re
from random import randint


def to_words(text):
    """Return a list of lower-cased words without interpunction.

    >>> to_words('A rabbit, a cat, and an eagle!')
    ['a', 'rabbit', 'a', 'cat', 'and', 'an', 'eagle']
    """
    text = text.lower()
    # Use regular expressions to replace all non-word characters by spaces.
    text_without_interpuction = re.sub('[\W_]', ' ',  text)
    words = text_without_interpuction.split()
    return words


# ------------- Task 11.1 --------------

def average_word_length(book):
    """Return average legnth of a word in a given book.

    >>> average_word_length('alice-in-wonderland.txt')
    3.93...
    """
    # TODO
    pass


# ------------- Task 11.2 --------------

def save_words_sorted_alphabetically(book, output_filename='words.txt'):
    """Save all words from the book sorted alphabetically to a new file.

    >>> save_words_sorted_alphabetically('alice-in-wonderland.txt')
    >>> with open('words.txt', 'r') as infile:
    ...     print(infile.read().split()[:5])
    ['a', 'abide', 'able', 'about', 'above']
    """
    # TODO
    pass


# ------------- Task 11.3 --------------

def save_words_sorted_by_length(book, output_filename='words.txt', min_length=3):
    """Save words having at least `min_length` letters sorted by length.

    >>> save_words_sorted_by_length('alice-in-wonderland.txt')
    """
    # TODO
    pass


def save_words_sorted_by_length_alphabetically(book, output_filename='words.txt', min_length=3):
    """Save words having at least `min_length` letters sorted by length.

    Words with the same length are sorted alphabetically.

    >>> save_words_sorted_by_length_alphabetically('alice-in-wonderland.txt')
    >>> with open('words.txt', 'r') as infile:
    ...     print(infile.read().split()[:5])
    ['act', 'ada', 'age', 'ago', 'air']
    """
    # TODO
    pass


# ------------- Task 11.4 --------------

def print_longest_words_in_book(book, n=5):
    """Compute n longest words and print them ordered by their length.

    Each word appears at most once in the list.
    Words with the same length are sorted alphabetically.

    >>> print_longest_words_in_book('alice-in-wonderland.txt', n=5)
    affectionately
    contemptuously
    disappointment
    multiplication
    circumstances
    """
    # TODO
    pass


# ------------- Task 11.5 --------------

def most_frequent_words_in_text(text, n=10, min_length=3):
    """Compute n most frequent words and print them ordered by frequency.

    >>> most_frequent_words_in_text(
    ... 'A rabbit, a cat,  an eagle, a rabbit, a cat, a rabbit and a rabbit!',
    ... n=2, min_length=3)
    rabbit 4
    cat 2
    """
    # TODO
    pass


def most_frequent_words_in_book(book, n=10, min_length=3):
    """Compute n most frequent words and print them ordered by frequency.

    Hint: Use most_frequent_words_in_text().

    >>> most_frequent_words_in_book('alice-in-wonderland.txt', n=4, min_length=5)
    alice 398
    little 128
    there 99
    about 94
    """
    # TODO
    pass


# ------------- Task 11.6 --------------

def compute_next_tokens_map(text):
    """Return a dictionary mapping tokens to list of next tokens.

    >>> next_tokens = compute_next_tokens_map('A rabbit, a rabbit, and a cat!')
    >>> next_tokens['a']
    ['rabbit,', 'cat!']
    >>> next_tokens['rabbit,']
    ['a', 'and']
    >>> next_tokens['cat!']
    []
    """
    # TODO
    pass


# ------------- Task 11.7 --------------

def compute_first_tokens(text):
    """Return a list of tokens that could appear at the beginning of a sentence

    >>> compute_first_tokens('First sentence. Another sentence? Yes!')
    ['First', 'Another', 'Yes!']
    """
    # Very simple heuristic: Just take tokens with upper-cased first letter.
    tokens = text.split()
    first_tokens = [token for token in tokens if token[0].isupper()]
    return first_tokens


def select_random(tokens):
    """Return a random token from a list of tokens.

    >>> select_random(['single'])
    'single'
    """
    # TODO
    pass


BOOKS = {
    'carroll': 'alice-in-wonderland.txt',
    'capek': 'devatero-pohadek.txt',
}


def imitate(author, n_words=50):
    """Generate new bestseller of given author generated on demand.

    Args:
        author: one of {'carroll', 'capek'}
        n_words: How many words to generate.

    Return:
        Generated text.

    Hints:
        Use compute_next_tokens_map(), compute_first_tokens(), select_random()
        and BOOKS dictionary.

    >>> generated_text = imitate('carroll')
    """
    # TODO
    pass


# ------------- Task 11.8 --------------

def imitate_sentences(author, n_sentences=10):
    """Generate n sentences imitating given author.

    Ideas for improvements (you can focus on Czech/English only):
    - use 2 previous tokens to select the new one
    - use 1-5 previous tokens (randomly) to select the new one
    - randomly insert sometimes words/sentences from recipes/textbooks
    - randomly replace some names/pronouns with names of your friends
    """
    pass


# ------------- main and test --------------

def main():
    print('\nCarroll:\n')
    print(imitate('carroll'))
    print('\nCapek:\n')
    print(imitate('capek'))


def test():
    """Check examples in docstrings.

    If the actual output matches the expected output, doesn't print anything.
    Otherwise, it prints an error message showing the mismatch.
    """
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)


if __name__ == '__main__':
    #main()
    test()
