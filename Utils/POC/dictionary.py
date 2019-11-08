"""
A dictionary that holds many words and translate between them.

File: dictionary.py
Description: A module that holds a dictionary. This dictionary holds many pair
             of words, and translate between those words.
"""


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

    def add_word(self, new_word_couple):
        """Add a new word couple to the dictionary.

        The new word will be added in a sorted manner. In case the word already
        appears in the dictionary, an error will raise.

        :new_word_couple: The new word couple to add to the object.
        :returns: None

        """
        # Validate that the word doesn't appear in the dictionary.
        all_translations = self.get_all_translations_to_translated_languege(
            new_word_couple.native_word)
        if new_word_couple.translated_word in all_translations:
            raise KeyError("Word is already in dictionary.")

        # Get the new index to add the word
        i = 0
        while (
                i < len(self.words) and
                new_word_couple.native_word > self.words[i].native_word):
            i += 1

        # Add the word.
        self.words.insert(i, new_word_couple)

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

    def get_all_translations_to_translated_languege(self, native_word):
        """Get all the translations of a given word.

        :native_word: The word in the native language
        :returns: A list with all the translations of the given word.

        """
        all_translations = []

        for current_word in self.words:
            if current_word.native_word == native_word:
                all_translations.append(current_word.translated_word)

        return all_translations

    def get_all_translations_to_native(self, translated_word):
        """Get all the translations of a given word to the native language.

        :translated_word: The word in the native language
        :returns: A list with all the translations of the given word.

        """
        all_translations = []

        for current_word in self.words:
            if current_word.translated_word == translated_word:
                all_translations.append(current_word.native_word)

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
