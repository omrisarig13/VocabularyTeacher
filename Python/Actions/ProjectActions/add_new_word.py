"""
An action that will add a new word pair to the dictionary.

File: add_new_word.py
"""

import qprompt

import word_couple

from Actions import menu_actions
from Utils import safe_ask


class AddNewWordAction(menu_actions.BaseAction):
    """An action that will Add a new word to the dictionary."""

    COMMAND_NAME = "Add New Word"
    HELP_TEXT = "Add the given new word to the dictionary."

    @staticmethod
    def add_new_word(dictionary):
        """Add a new word to the dictionary.

        :dictionary: The dictionary to add the word to.
        :returns: True if the user wanted to add new word, False otherwise.

        :note: The return value indicate only the user's intention. In case the
        word was not added (for example, if it already was in the dictionary),
        the function will still return True.
        :note: The function get all the word's parameters from the user.

        """
        print("Insert the words as asked for. To cancel, put -1 as any field.")

        native_word = safe_ask.safe_ask(
            qprompt.ask_str, "Insert the native word")
        learned_word = safe_ask.safe_ask(
            qprompt.ask_str, "Insert the learned word")
        known_level = safe_ask.safe_ask(
            qprompt.ask_int,
            "Insert the known level",
            0,
            vld=list(range(-1, word_couple.WordCouple.MAX_LEVEL + 1)))

        # In case the one of the parameters was set to -1 it also means that
        # the user didn't want to add the word, simply exit the function.
        if known_level == -1 or native_word == "-1" or learned_word == "-1":
            print("Not adding any new word.")
            return False

        new_word = word_couple.WordCouple(native_word, learned_word,
                                          known_level)
        try:
            dictionary.add_word(new_word)
        except KeyError as dictionary_error:
            print(dictionary_error)

        return True

    def run_command(self, menu_context):
        """Run the command that will add the new word to the dictionary.

        :menu_context: The context of the menu to add the dictionary to.

        :Note: This functions adds the new word to the dictionary.

        """
        # Get the dictionary (and validate it exists).
        dictionary = menu_context.get("dictionary", None)
        if dictionary is None:
            print("Menu does not have a dictionary")
            qprompt.pause()
            return

        # Add the new word.
        self.add_new_word(dictionary)

        # Make sure the user sees the output before ending the action.
        qprompt.pause()


class BulkAddNewWordAction(menu_actions.BaseAction):
    """An action that will add words to the dictionary."""

    COMMAND_NAME = "Bulk Add New Words"
    HELP_TEXT = "Add a bulk of new words to the dictionary."

    def run_command(self, menu_context):
        """Run the command that will add a bulk of new words to the dictionary.

        :menu_context: The context of the menu to add the dictionary to.

        :Note: This functions adds the new word to the dictionary.

        """
        # Get the dictionary (and validate it exists).
        dictionary = menu_context.get("dictionary", None)
        if dictionary is None:
            print("Menu does not have a dictionary")
            qprompt.pause()
            return

        print("Add all the wanted new words to the dictionary. "
              "To end the input, stop inserting words "
              "(by exiting as prompt in add word).")

        # As long as the user has add a new word, continue to add words.
        while AddNewWordAction.add_new_word(dictionary):
            pass

        # Make sure the user sees the output before ending the action.
        qprompt.pause()
