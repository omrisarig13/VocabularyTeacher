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
        new_native_word = new_word_couple.native_word
        new_translated_word = new_word_couple.translated_word
        main_new_native_word = new_native_word.get_most_common_spelling()
        all_new_native_words = new_native_word.get_all_word_spellings()

        # Validate that the word doesn't appear in the dictionary.
        all_translations = self.get_all_translations_to_learned(
            all_new_native_words)

        all_word_translations = new_translated_word.get_all_word_spellings()
        for current_word_translation in all_word_translations:
            if current_word_translation in all_translations:
                raise KeyError("Word is already in dictionary.")

        # Get the new index to add the word
        i = 0
        while (
                i < len(self.words) and
                main_new_native_word > (
                    self.words[i].native_word.get_most_common_spelling())):
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

    def get_all_translations_to_learned(self, native_words):
        """Get all the translations of given words.

        :native_words: A list with all the native words to get the translation
         of.
        :returns: A list with all the translations of the given words.

        """
        all_translations = []

        for current_word in self.words:
            current_native_words = (
                current_word.native_word.get_all_word_spellings())
            for current_native_word in current_native_words:
                if current_native_word in native_words:
                    all_translations.extend(
                        current_word.translated_word.get_all_word_spellings())
                    break

        return all_translations

    def get_all_translations_to_native(self, translated_words):
        """Get all the translations of a given word to the native language.

        :translated_words: A list with all the translation of the given word.
        :returns: A list with all the translations of the given word.

        """
        all_translations = []

        for current_word in self.words:
            current_translations = (
                current_word.translated_word.get_all_word_spellings())
            for current_translated_word in current_translations:
                if current_translated_word in translated_words:
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

    def get_word(self, native_word, translated_word):
        """Get the word couple from the dictionary.

        :native_word: The word in the native language
        :translated_word: the word in the translated language.
        :returns: The word from the dictionary.

        """
        for current_word in self.words:
            all_native_word_spelling = (
                current_word.native_word.get_all_word_spellings())
            all_translation_word_spelling = (
                current_word.translated_word.get_all_word_spellings())
            if (
                    native_word in all_native_word_spelling and
                    translated_word in current_word.get_translated_word()):
                return current_word

        raise KeyError("Word not in dictionary.")

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
