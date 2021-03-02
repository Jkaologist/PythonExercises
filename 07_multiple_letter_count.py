def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    counts = dict()
    for letter in phrase:
        if counts.get(letter) is None:
            counts[letter] = 1
        else:
            counts[letter] += 1
    return counts
