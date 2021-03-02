def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_str = ''
    for letter in phrase:
        if (letter == to_swap.upper()) or (letter == to_swap.lower()):
            new_str += letter.swapcase()
        else:
            new_str += letter
    return new_str
