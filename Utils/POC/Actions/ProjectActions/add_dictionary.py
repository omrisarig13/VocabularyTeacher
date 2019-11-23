"""
An action that will add a dictionary to the menu.

File: add_dictionary.py
"""

import qprompt

import dictionary

import menu
from Actions import menu_actions


class AddDictionaryAction(menu_actions.BaseAction):
    """An action that will add a new dictionary to the program."""

    COMMAND_NAME = "add_dictionary"
    HELP_TEXT = "Add a new dictionary to the menu."
    ARGUMENTS = """None"""
    USAGE = "{command_name}".format(command_name=COMMAND_NAME)

    def run_command(self, menu_context, *args, **kwargs):
        """Run the command that will add the dictionary to the menu.

        :menu_context: The context of the menu to add the dictionary to.
        :returns: True to make the menu continue to run

        :Note: This functions adds the dictionary to the menu context.
        """
        if menu_context.get("dictionary", None):
            raise menu.InvalidCommand("Menu already has a dictionary.")

        native_language = qprompt.ask_str(
            "Insert the native language of the dictionary")
        learned_language = qprompt.ask_str(
            "Insert the learned language of the dictionary")

        new_dictionary = dictionary.Dictionary(native_language,
                                               learned_language)
        menu_context["dictionary"] = new_dictionary

        return True
