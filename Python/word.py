"""
A single word object.

File: word.py
Description: A simple word object for the project.
"""

from __future__ import annotations


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

    def is_same_word(self, word_to_check: str):
        """Check if the given word is the same as the current word.

        The new word will be the same as the current word in case it is one
        of the possible spelling options of the current word.

        :word_to_check: The word to check
        :returns: True if the word is one of the word's spellings, False
         otherwise.

        """
        return word_to_check in self._spellings

    def is_word_same_word(self, word_to_check: Word):
        """Check if the given Word object is the same as the current word.

         Two words objects are the same in case they have at least one common
         spelling between them.

        :word_to_check: The word to check.
        :returns: True if the words are the same, False otherwise.

        """
        return any([self.is_same_word(current_spelling) for current_spelling in
                    word_to_check.get_all_word_spellings()])

    def add_secondary_spelling(self, new_spelling):
        """Add a new secondary spelling to the word.

        :new_spelling: The new spelling of the word.
        :returns: None

        """
        if new_spelling not in self._spellings:
            self._spellings.append(new_spelling)

    def add_primary_spelling(self, new_spelling):
        """Add a new primary spelling to the word.

        :new_spelling: The new spelling of the word.
        :returns: None

        :note: The function will not change the word in case it is already
         a given spelling of the word.

        """
        if new_spelling not in self._spellings:
            self._spellings.insert(0, new_spelling)
