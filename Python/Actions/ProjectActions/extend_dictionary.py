"""
Extend the current dictionary with more words loaded from another dictionary.

File: load_dictionary.py
"""

import qprompt

from Actions import menu_actions
from Actions.ProjectActions import load_dictionary
from Utils import safe_ask


class ExtendDictionaryAction(menu_actions.BaseAction):
    """An action that will Extend the dictionary with the new loaded one."""

    COMMAND_NAME = "Extend Dictionary"
    HELP_TEXT = "Extend the dictionary to with another one."

    def run_command(self, menu_context):
        """Extend the dictionary in the context with the new loaded one.

        :menu_context: The context of the menu.

        """
        if menu_context.get("dictionary", None) is None:
            print("Can't extend dictionary when there isn't one.")
            qprompt.pause()
            return

        file_name = safe_ask.safe_ask(
            qprompt.ask_str,
            "Insert the new name of the dictionary")
        dictionary = menu_context["dictionary"]

        load_action = load_dictionary.LoadDictionaryAction.load_dictionary_file
        new_dictionary = load_action(file_name)

        dictionary.extend(new_dictionary)
