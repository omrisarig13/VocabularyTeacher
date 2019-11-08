"""
Extend the current dictionary with more words loaded from another dictionary.

File: load_dictionary.py
"""

import menu
from Actions import menu_actions
from Actions.ProjectActions import load_dictionary


class ExtendDictionaryAction(menu_actions.BaseAction):
    """An action that will Extend the dictionary with the new loaded one."""

    COMMAND_NAME = "extend_dictionary"
    HELP_TEXT = "Extend the dictionary to with another one."
    ARGUMENTS = """
            file_name - The name of the file with the new dictionary.
    """
    USAGE = "{command_name} file_name".format(command_name=COMMAND_NAME)

    def run_command(self, menu_context, *args, **kwargs):
        """Extend the dictionary in the context with the new loaded one.

        :menu_context: The context of the menu.
        :*args: The special arguments for the command. It will include the
                name of the file to load the dictionary from.
        :returns: True to make the menu continue to run

        """
        if len(args) != 1:
            raise menu.InvalidCommand(
                "Invalid number of arguments for command. Read the help")

        if menu_context.get("dictionary", None) is None:
            raise menu.InvalidCommand(
                "Can't extend dictionary when there isn't one.")

        file_name = args[0]
        dictionary = menu_context["dictionary"]

        load_action = load_dictionary.LoadDictionaryAction.load_dictionary_file
        new_dictionary = load_action(file_name)

        dictionary.extend(new_dictionary)

        return True
