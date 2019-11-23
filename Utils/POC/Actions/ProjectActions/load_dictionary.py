"""
An action that will load a dictionary from a file on the disk.

File: load_dictionary.py
"""

import pickle

import qprompt

import menu
from Actions import menu_actions


class LoadDictionaryAction(menu_actions.BaseAction):
    """An action that will Load the dictionary of the menu from a file."""

    COMMAND_NAME = "load_dictionary"
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

    def run_command(self, menu_context, *args, **kwargs):
        """Run the command that will load the dictionary from the file.

        :menu_context: The context of the menu to add the dictionary to.
        :*args: The special arguments for the command. It will include the
                name of the file to load the dictionary from.
        :returns: True to make the menu continue to run

        :Note: This functions adds the dictionary to the context of the menu.

        """
        if menu_context.get("dictionary", None):
            raise menu.InvalidCommand("Menu already has a dictionary.")

        file_name = qprompt.ask_str("Insert the file name of the dictionary")

        menu_context["dictionary"] = self.load_dictionary_file(file_name)

        return True
