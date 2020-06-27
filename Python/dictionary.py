"""
A dictionary that holds many words and translate between them.

File: dictionary.py
Description: A module that holds a dictionary. This dictionary holds many pair
             of words, and translate between those words.
"""

import qprompt

import word_couple


class Dictionary():
    """A dictionary that holds many word couples."""

    def __init__(self, native_language, translated_language):
        """Initialize a new object of a dictionary.

        :native_language: The native language used in the dictionary.
        :translated_language: The translated language used in the dictionary.
        """
        self.words = []
        self.native_language = native_language
        self.translated_language = translated_language

    #TODO: Refactor this function to get natvie and translated instead of word.
    def add_word(self, new_word_couple, should_ask_close_words=True):
        """Add a new word couple to the dictionary.

        The new word will be added in a sorted manner. In case the word already
        appears in the dictionary, an error will raise.

        :new_word_couple: The new word couple to add to the object.
        :should_ask_close_words: True if the function should try to find close
         words to the new function and ask the user to merge them, False
         otherwise.
        :returns: None

        """
        # Validate that the word doesn't appear in the dictionary.
        self._validate_word_not_in_dict(new_word_couple)

        was_word_added = False
        if should_ask_close_words:
            was_word_added = self._add_word_by_close_words(new_word_couple)

        if not was_word_added:
            # Get the new index to add the word
            i = self._get_new_word_index(
                new_word_couple.native_word.get_most_common_spelling())

            # Add the word.
            self.words.insert(i, new_word_couple)

    def _add_word_by_close_words(self, new_word_couple):
        """Add the new word by its close words.

        The function checks if there are any close words to the current word,
        and in case there are it asks the user if the new word should be
        extended as part of them.

        :new_word_couple: The new word couple to try to add.
        :returns: True if the word was added to one of its closed words, False
         otherwise.

        """
        for current_word in self.words:
            if current_word.is_word_close(new_word_couple):
                print("The current word is close to the word {}.".format(
                    current_word))
                if qprompt.ask_yesno(
                        "Do you want to add this as the same word? [Y/n]",
                        dft=True):
                    is_primary = qprompt.ask_yesno(
                        "is this the primary spelling of the word? [y/N]",
                        dft=False)
                    current_word.extend_word(new_word_couple, is_primary)
                    return True

        return False

    def _validate_word_not_in_dict(self, new_word_couple):
        """Validate that the current word is not already in the dict.

        :new_word_couple: The new word to check in the dictionary.
        :returns: None
        :raises: KeyError In case the word is already in the dictionary.

        """
        word_from_dictionary = self.get_word_from_word(new_word_couple)
        if word_from_dictionary is not None:
            raise KeyError("Word is already in dictionary ({}).".format(
                word_from_dictionary))

    def _get_new_word_index(self, native_word):
        """Get the index in which to insert the new word couple.

        :new_word_couple: The new native word to add.
        :returns: The index in the dictionary to add the native word to.

        """
        i = 0

        while (
                i < len(self.words) and
                native_word > (
                    self.words[i].native_word.get_most_common_spelling())):
            i += 1

        return i

    def __str__(self):
        """Create an string presentation of the dictionary.

        :returns: The string implementation of the dictionary.

        """
        string_dict = "Dictionary from {} to {}.\n".format(
            self.native_language,
            self.translated_language)
        string_dict += "Dictionary contains {} words.\n".format(
            len(self.words))

        string_dict += "Dictionary data:\n"
        for current_word in self.words:
            string_dict += "\t{}\n".format(str(current_word))

        return string_dict

    def get_all_translations_to_learned(self, native_words: list):
        """Get all the translations of given words.

        :native_words: A list with all the native words to get the translation
         of.
        :returns: A list with all the translations of the given words.

        """
        all_translations: list = []

        for current_word in self.words:
            for current_native_word in native_words:
                if current_word.native_word.is_same_word(current_native_word):
                    all_translations.extend(
                        current_word.translated_word.get_all_word_spellings())
                    break

        return all_translations

    def get_all_translations_to_native(self, translated_words: list):
        """Get all the translations of a given word to the native language.

        :translated_words: A list with all the translation of the given word.
        :returns: A list with all the translations of the given word.

        """
        all_translations: list = []

        for current_word in self.words:
            for current_translated_word in translated_words:
                if current_word.translated_word.is_same_word(
                        current_translated_word):
                    all_translations.extend(
                        current_word.native_word.get_all_word_spellings())
                    break

        return all_translations

    def extend(self, second_dictionary):
        """Concatenate the second dictionary into this one.

        Move over all the words in the second dictionary and add all of them
        into the current dictionary. In case of a word that appears in multiple
        dictionaries, it's level will stay the same as the one in this
        dictionary.

        :second_dictionary: The dictionary to add into this one.
        :returns: None

        """
        # Validate that the dictionaries can be concatenated.
        if (
                self.native_language != second_dictionary.native_language or
                (self.translated_language !=
                 second_dictionary.translated_language)):
            raise ValueError(
                "Can't extend dictionaries with different languages")

        # Add all the words from the second dictionary into this one.
        for current_word in second_dictionary.words:
            try:
                self.add_word(current_word)
            except KeyError:
                pass

    def get_word(self, native_word: str, translated_word: str):
        """Get the word couple from the dictionary.

        :native_word: The word in the native language
        :translated_word: the word in the translated language.
        :returns: The word from the dictionary.

        """
        for current_word in self.words:
            if current_word.is_same_word(native_word, translated_word):
                return current_word

        raise KeyError("Word not in dictionary.")

    def get_word_from_word(self, word_to_get: word_couple.WordCouple):
        """Get the same word couple from the dictionary.

        :word_to_get: The word to get from the dictionary.
        :returns: The word from the dictionary. None in case the word doesn't
         exist in the dicitonary.

        """
        for current_word in self.words:
            if current_word.is_word_couple_same(word_to_get):
                return current_word

        return None

    def get_words_from_level(self, level):
        """Get all the words from some level in the dictionary.

        :level: The level to get the words from.
        :returns: A list with all the words from this level.

        """
        words_from_level = []

        for current_word in self.words:
            if current_word.word_known_level == level:
                words_from_level.append(current_word)

        return words_from_level

    def print_summary(self):
        words_above_level_one = 0
        for current_level in range(5):
            current_number_of_words = len(self.get_words_from_level(current_level))
            print(f"{current_number_of_words} words from level {current_level}")
            if current_level > 0:
                words_above_level_one += current_number_of_words
        print(f"There are {words_above_level_one} words above level one")
        print(f"There are {len(self.words)} words in the dictionary.")

    def delete_word(self, word_index):
        """Delete a word from the dictionary.

        :word_index: The index of the word to delete from the dictionary.

        """
        self.words.pop(word_index)

    def get_word_by_index(self, word_index):
        """Get the word in the given index.

        :word_index: The index of the word to get.

        """
        return self.words[word_index]

