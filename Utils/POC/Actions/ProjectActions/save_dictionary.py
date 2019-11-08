"""
An action that will save a dictionary to a file on the disk.

File: save_dictionary.py
"""

import pickle

import menu
from Actions import menu_actions


class SaveDictionaryAction(menu_actions.BaseAction):
    """An action that will save the dictionary of the menu to a file."""

    COMMAND_NAME = "save_dictionary"
    HELP_TEXT = "Save the dictionary to a give file."
    ARGUMENTS = """
            file_name - The file name to save the dictionary to
    """
    USAGE = "{command_name} file_name".format(command_name=COMMAND_NAME)

    def run_command(self, menu_context, *args, **kwargs):
        """Run the command that will save the dictionary to the file.

        :menu_context: The context of the menu.
        :*args: The special arguments for the command. It will include the
                name of the file to save the dictionary into.
        :returns: True to make the menu continue to run

        """
        if len(args) != 1:
            raise menu.InvalidCommand(
                "Invalid number of arguments for command. Read the help")

        if menu_context.get("dictionary", None) is None:
            raise menu.InvalidCommand("Menu doesn't have a dictionary.")

        file_name = args[0]

        with open(file_name, "wb") as dictionary_file:
            pickle.dump(menu_context["dictionary"], dictionary_file)

        return True
