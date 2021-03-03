def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    return_phrase = []
    lst = phrase.split()
    for item in lst:
        return_phrase.append(item.capitalize())
    return " ".join(return_phrase)
