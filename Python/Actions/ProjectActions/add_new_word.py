"""
An action that will add a new word pair to the dictionary.

File: add_new_word.py
"""

import qprompt

import word_couple

from Actions import menu_actions


class AddNewWordAction(menu_actions.BaseAction):
    """An action that will Add a new word to the dictionary."""

    COMMAND_NAME = "Add New Word"
    HELP_TEXT = "Add the given new word to the dictionary."

    def run_command(self, menu_context):
        """Run the command that will add the new word to the dictionary.

        :menu_context: The context of the menu to add the dictionary to.

        :Note: This functions adds the new word to the dictionary.

        """
        if menu_context.get("dictionary", None) is None:
            print("Menu does not have a dictionary")
            qprompt.pause()
            return

        dictionary = menu_context["dictionary"]

        print("Insert the words as asked for. To cancel, put -1 as any field.")

        native_word = qprompt.ask_str("Insert the native word")
        learned_word = qprompt.ask_str("Insert the learned word")
        known_level = qprompt.ask_int(
            "Insert the known level",
            0,
            vld=list(range(-1, word_couple.WordCouple.MAX_LEVEL + 1)))

        # In case the one of the parameters was set to -1 it also means that
        # the user didn't want to add the word, simply exit the function.
        if known_level == -1 or native_word == "-1" or learned_word == "-1":
            return

        new_word = word_couple.WordCouple(native_word, learned_word,
                                          known_level)
        try:
            dictionary.add_word(new_word)
        except KeyError as dictionary_error:
            print(dictionary_error)
            qprompt.pause()
