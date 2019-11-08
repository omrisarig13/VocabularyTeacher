"""
An action that will print the dictionary to the user.

File: print_dictionary.py
"""

import menu
from Actions import menu_actions


class PrintDictionaryAction(menu_actions.BaseAction):
    """An action that will print the dictionary to the user."""

    COMMAND_NAME = "print_dictionary"
    HELP_TEXT = "Print the dictionary to the user."
    ARGUMENTS = """None"""
    USAGE = "{command_name}".format(command_name=COMMAND_NAME)

    def run_command(self, menu_context, *args, **kwargs):
        """Run the command that will print the dictionary to the user.

        :menu_context: The context of the menu to add the dictionary to.
        :*args: The special arguments for the command. Not used in this
                function.
        :returns: True to make the menu continue to run

        :Note: The function prints the dictionary to the user.
        """
        if menu_context.get("dictionary", None) is None:
            raise menu.InvalidCommand("Menu does not have a dictionary")

        print(menu_context["dictionary"])

        return True
