"""
A couple of Words object in multiple languages.

File: word_couple.py
Description: A translation of words between native language and new learned
             language.
"""

import word

class WordCouple():
    """A couple of words, one in each language.

    This is the most basic object in the project, saving a word and its
    translation.
    """

    MAX_LEVEL = 4
    ANSWERS_PER_LEVEL = 3

    def __init__(self, native_word, translated_word, word_known_level=0,
                 lower_case=True):
        """Initialize the object.

        :native_word: The word in the native language.
        :translated_word: The translation of the word in the new learned
        language.
        :word_known_level: The level in which the word is already known. For
                           new words this value should remain empty.
        :lower_case: True if you want to save the lower case of the word, False
                     otherwise.

        """
        if lower_case:
            native_word = native_word.lower()
            translated_word = translated_word.lower()
        self.native_word = word.Word(native_word)
        self.translated_word = word.Word(translated_word)
        self.word_known_level = word_known_level
        self._current_stage_in_learned_level = 0

    def __str__(self):
        """Return the string representation of the object.

        :returns: The string representation of the object.

        """
        return "{} : {} [{}]".format(str(self.native_word),
                                     str(self.translated_word),
                                     self.word_known_level)

    def answered_right(self):
        """Update the word level after right answer.

        :returns: None

        """
        if self.word_known_level < self.MAX_LEVEL:
            self._current_stage_in_learned_level += 1

            if self._current_stage_in_learned_level >= self.ANSWERS_PER_LEVEL:
                self.word_known_level += 1
                self._current_stage_in_learned_level = 0

    def answered_wrong(self):
        """Update the word level after wrong answer.

        :returns: None

        """
        if self._current_stage_in_learned_level > (
                -1 * self.ANSWERS_PER_LEVEL):
            self._current_stage_in_learned_level -= 1
        else:
            if self.word_known_level > 0:
                self.word_known_level -= 1
                self._current_stage_in_learned_level = 0

    def reset_knowledge(self):
        """Reset the knowladge of the word, to start learning it again.

        This function should be used to completely reset the state of a given
        word, making it as if the word was just now created.

        :returns: None

        """
        self._current_stage_in_learned_level = 0
        self.word_known_level = 0
