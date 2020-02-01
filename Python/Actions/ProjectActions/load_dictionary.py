"""
An action that will load a dictionary from a file on the disk.

File: load_dictionary.py
"""

import pickle

import qprompt

from Actions import menu_actions
from Utils import safe_ask


class LoadDictionaryAction(menu_actions.BaseAction):
    """An action that will Load the dictionary of the menu from a file."""

    COMMAND_NAME = "Load Dictionary"
    HELP_TEXT = "Load the dictionary to a give file."
    ARGUMENTS = """None"""
    USAGE = "{command_name}".format(command_name=COMMAND_NAME)

    @staticmethod
    def load_dictionary_file(file_name):
        """Load the dictionary from the disk.

        :file_name: The name of the dictionary file.
        :returns: The dictionary loaded from the disk.

        """
        with open(file_name, "rb") as dictionary_file:
            loaded_dictionary = pickle.load(dictionary_file)

        return loaded_dictionary

    def run_command(self, menu_context):
        """Run the command that will load the dictionary from the file.

        :menu_context: The context of the menu to add the dictionary to.

        :Note: This functions adds the dictionary to the context of the menu.

        """
        if menu_context.get("dictionary", None):
            print("Menu already has a dictionary.")
            qprompt.pause()
            return

        file_name = safe_ask.safe_ask(
            qprompt.ask_str, "Insert the file name of the dictionary")

        menu_context["dictionary"] = self.load_dictionary_file(file_name)
        menu_context["dictionary_name"] = file_name

        return
