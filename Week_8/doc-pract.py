def maxValue(d):
    """ Takes a dictionary d and returns the maximum element value and its
        corresponding key. Raises a TypeError if any of the values are not
        comparable to each other.

        >>> maxValue({'a': 12, 3: 45})
        (3, 45)
        >>> maxValue({}) is None
        True
        >>> maxValue({33: 34, -1: 600, 'xyz': 2000.4})
        ('xyz', 2000.4)
        >>> maxValue({1: 'abc', 2: 'xyz', 3: 'ghijkl'})
        (2, 'xyz')
        >>> maxValue({1:'a', 2:3}) # doctest:+ELLIPSIS
        Traceback (most recent call last):
            ...
        TypeError:...
        # Hint: d.values() is a sequence of all the values in dictionary d
    #       try using this along with built-in function max

    """
    
    
    return max(d.values())

maxValue({33: 34, -1: 600, 'xyz': 2000.4})