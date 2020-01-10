"""
A single word object.

File: word.py
Description: A simple word object for the project.
"""


class Word():
    """A basic word for the project."""

    def __init__(self, main_spelling):
        """Initialize the values of the word.

        :main_spelling: The most common spelling of the given word.
        """
        self._spellings = [main_spelling]

    def get_most_common_spelling(self):
        """Get the most common spelling of the given word.

        :returns: The most common spelling of the given word.
        """
        return self._spellings[0]

    def get_all_word_spellings(self):
        """Get all the spellings of the given word.

        :returns: All the spellings of the given word.
        """
        return self._spellings

    def __str__(self):
        """Return the string representation of the object.

        :returns: The string representation of the object.

        """
        return str(self._spellings)

