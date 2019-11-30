"""
An action that will save a dictionary to a file on the disk.

File: save_dictionary.py
"""

import pickle

import qprompt

from Actions import menu_actions


class SaveDictionaryAction(menu_actions.BaseAction):
    """An action that will save the dictionary of the menu to a file."""

    COMMAND_NAME = "Save Dictionary"
    HELP_TEXT = "Save the dictionary to a give file."

    def run_command(self, menu_context):
        """Run the command that will save the dictionary to the file.

        :menu_context: The context of the menu.

        """
        if menu_context.get("dictionary", None) is None:
            print("Menu doesn't have a dictionary.")
            qprompt.pause()
            return

        file_name = qprompt.ask_str(
            "Insert the file name to save the dictionary into")

        with open(file_name, "wb") as dictionary_file:
            pickle.dump(menu_context["dictionary"], dictionary_file)
