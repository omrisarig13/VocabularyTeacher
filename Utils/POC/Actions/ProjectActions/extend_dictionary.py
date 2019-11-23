"""
Extend the current dictionary with more words loaded from another dictionary.

File: load_dictionary.py
"""

import qprompt

import menu
from Actions import menu_actions
from Actions.ProjectActions import load_dictionary


class ExtendDictionaryAction(menu_actions.BaseAction):
    """An action that will Extend the dictionary with the new loaded one."""

    COMMAND_NAME = "extend_dictionary"
    HELP_TEXT = "Extend the dictionary to with another one."
    ARGUMENTS = """None"""
    USAGE = "{command_name}".format(command_name=COMMAND_NAME)

    def run_command(self, menu_context, *args, **kwargs):
        """Extend the dictionary in the context with the new loaded one.

        :menu_context: The context of the menu.
        :returns: True to make the menu continue to run

        """
        if menu_context.get("dictionary", None) is None:
            raise menu.InvalidCommand(
                "Can't extend dictionary when there isn't one.")

        file_name = qprompt.ask_str("Insert the new name of the dictionary")
        dictionary = menu_context["dictionary"]

        load_action = load_dictionary.LoadDictionaryAction.load_dictionary_file
        new_dictionary = load_action(file_name)

        dictionary.extend(new_dictionary)

        return True
