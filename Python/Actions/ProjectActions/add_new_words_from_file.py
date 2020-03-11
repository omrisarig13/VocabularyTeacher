"""
An action that will add new words from a yaml file.

File: add_new_words_from_file.py
"""

import qprompt
import yaml

import word_couple

from Actions import menu_actions
from Utils import safe_ask


class AddNewWordsFromFileAction(menu_actions.BaseAction):
    """An action that will add a file full of words to the dictionary."""

    COMMAND_NAME = "Add New Words from file"
    HELP_TEXT = "Read the given yaml file, parse it and add all its words "\
                "to the dictionary."

    @staticmethod
    def add_current_word(dictionary, native_word, learned_word):
        """Add the current word to the dictionary.

        :dictionary: The dictionary to add the words into.
        :native_word: The native value of the word.
        :learned_word: The learned value of the word.
        :returns: None

        """
        new_word = word_couple.WordCouple(native_word, learned_word)
        try:
            dictionary.add_word(new_word)
        except KeyError as dictionary_error:
            print(dictionary_error)

    @staticmethod
    def load_yaml_file(yaml_file_path):
        """Load the given yaml file into a python object.

        :yaml_file_path: The path to the yaml file to load.
        :returns: The yaml object.

        """
        with open(yaml_file_path, "r") as yaml_file:
            yaml_object = yaml.safe_load(yaml_file)
        return yaml_object

    def add_new_words(self, dictionary, file_to_load):
        """Add words from the given file to the dictionary.

        :dictionary: The dictionary to add the words into.
        :file_to_load: The yaml file with all the words. The file should
                       contain list of dictionaries, every inner dictionary
                       contains the native word and then the learned word. This
                       is done this way in order to let the file have multiple
                       definitions with the same native word, without them
                       running over one another.
        :returns: None

        """
        all_words = self.load_yaml_file(file_to_load)

        for current_word_pair in all_words:
            for (current_native_word, current_learned_word) \
                    in current_word_pair.items():
                print(
                    f"Adding new word: {current_native_word}:"
                    f"{current_learned_word}")
                self.add_current_word(dictionary, current_native_word,
                                      current_learned_word)

        return True

    def run_command(self, menu_context):
        """Run the command that will add load the file to the dict.

        :menu_context: The context of the menu to add the dictionary to.

        :Note: This functions adds the new words to the dictionary.

        """
        # Get the dictionary (and validate it exists).
        dictionary = menu_context.get("dictionary", None)
        if dictionary is None:
            print("Menu does not have a dictionary")
            qprompt.pause()
            return

        # Get the name of the yaml file.
        file_with_words = safe_ask.safe_ask(
            qprompt.ask_str,
            "Insert the name of the file with the words")

        # Add the new word.
        self.add_new_words(dictionary, file_with_words)

        # Make sure the user sees the output before ending the action.
        qprompt.pause()
