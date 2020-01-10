"""
Surround the ask functions (ask_str, ask_int...) try...catch.

This module was created to make sure that all the ask method will be safe, and
won't raise any exceptions because of user input.

File: safe_ask.py
"""


def safe_ask(function, *args, **kwargs):
    """Get input safely from the user.

    :function: The ask function to run.
    :*args: The args to the given ask function.
    :**kwargs: The args to the given ask function.
    :returns: The return from the ask function.

    """
    value_got = None
    got_valid_input = False

    while not got_valid_input:
        try:
            # Make the value back none, in case the previous action stopped
            # prematurely but change the value.
            value_got = None
            value_got = function(*args, **kwargs)
            got_valid_input = True
        except UnicodeDecodeError:
            # In case the user has inserted invalid string, simply continue the
            # loop (which will ask for the input again).
            pass

    return value_got
