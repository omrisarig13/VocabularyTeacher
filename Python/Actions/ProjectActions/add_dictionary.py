"""
An action that will add a dictionary to the menu.

File: add_dictionary.py
"""

import qprompt

import dictionary

from Actions import menu_actions
from Utils import safe_ask


class AddDictionaryAction(menu_actions.BaseAction):
    """An action that will add a new dictionary to the program."""

    COMMAND_NAME = "Add Dictionary"
    HELP_TEXT = "Add a new dictionary to the menu."

    def run_command(self, menu_context):
        """Run the command that will add the dictionary to the menu.

        :menu_context: The context of the menu to add the dictionary to.

        :Note: This functions adds the dictionary to the menu context.
        """
        if menu_context.get("dictionary", None):
            print("Menu already has a dictionary.")
            qprompt.pause()
            return

        native_language = safe_ask.safe_ask(
            qprompt.ask_str,
            "Insert the native language of the dictionary")
        learned_language = safe_ask.safe_ask(
            qprompt.ask_str,
            "Insert the learned language of the dictionary")

        new_dictionary = dictionary.Dictionary(native_language,
                                               learned_language)
        menu_context["dictionary"] = new_dictionary
