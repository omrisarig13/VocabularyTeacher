"""
An action that will delete a word from the dictionary.

File: delete_word.py
"""

import consolemenu
import qprompt

from Actions import menu_actions
from Utils import safe_ask


class DeleteWordAction(menu_actions.BaseAction):
    """An action that will delete a word from the dictionary."""

    COMMAND_NAME = "Delete Word"
    HELP_TEXT = "Delete a word from the dictionary."

    def run_command(self, menu_context):
        """Run the command that will delete a word from the dictionary.

        :menu_context: The context of the menu to add the dictionary to.
        """
        if menu_context.get("dictionary", None) is None:
            print("Menu does not have a dictionary")
            qprompt.pause()
            return

        dictionary = menu_context["dictionary"]

        word_index_to_remove = safe_ask.safe_ask(
            qprompt.ask_int,
            "Insert the index of the word to remove")

        word_to_remove = dictionary.get_word_by_index(word_index_to_remove)
        if qprompt.ask_yesno(
            f"Do you want to remove the word \"{word_to_remove}?\"",
            dft=False):
            dictionary.delete_word(word_index_to_remove)
            print("Word removed")
        else:
            print("Word not removed")

        qprompt.pause()
