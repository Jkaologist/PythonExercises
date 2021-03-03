def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    if command == "remove" and location == "beginning" and value is None:
        first = lst[0]
        lst.remove(lst[0]) # pop can pop whatever at any index pass in the index
        return first
    elif command == "remove" and location == "end" and value is None:
        last = lst[-1]
        lst.remove(lst[-1]) # pop is a possibility
        return last
    if value is not None and command == "add" and location == "beginning":
        lst.insert(0, value)
        return lst
    if value is not None and command == "add" and location == "end":
        lst.append(value)
        return lst
