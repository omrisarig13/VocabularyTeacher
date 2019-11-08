"""
An action that will add a dictionary to the menu.

File: add_dictionary.py
"""

import dictionary

import menu
from Actions import menu_actions


class AddDictionaryAction(menu_actions.BaseAction):
    """An action that will add a new dictionary to the program."""

    COMMAND_NAME = "add_dictionary"
    HELP_TEXT = "Add a new dictionary to the menu."
    ARGUMENTS = """
            native_language - The native language in the dictionary.
            learned_language - The languege to learn using the dictionary.
    """
    USAGE = "{command_name} native_language learned_language".format(
        command_name=COMMAND_NAME)

    def run_command(self, menu_context, *args, **kwargs):
        """Run the command that will add the dictionary to the menu.

        :menu_context: The context of the menu to add the dictionary to.
        :*args: The special arguments for the command. It will include the
                native language and the learned language of it.
        :returns: True to make the menu continue to run

        :Note: This functions adds the dictionary to the menu context.
        """
        if len(args) != 2:
            raise menu.InvalidCommand(
                "Invalid number of arguments for command. Read the help")

        if menu_context.get("dictionary", None):
            raise menu.InvalidCommand("Menu already has a dictionary.")

        native_language = args[0]
        learned_language = args[1]

        new_dictionary = dictionary.Dictionary(native_language,
                                               learned_language)
        menu_context["dictionary"] = new_dictionary

        return True
