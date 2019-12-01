"""
An action that will print the dictionary to the user.

File: print_dictionary.py
"""

import consolemenu
import qprompt

from Actions import menu_actions


class PrintDictionaryAction(menu_actions.BaseAction):
    """An action that will print the dictionary to the user."""

    COMMAND_NAME = "Print Dictionary"
    HELP_TEXT = "Print the dictionary to the user."

    def run_command(self, menu_context):
        """Run the command that will print the dictionary to the user.

        :menu_context: The context of the menu to add the dictionary to.

        :Note: The function prints the dictionary to the user.
        """
        if menu_context.get("dictionary", None) is None:
            print("Menu does not have a dictionary")
            qprompt.pause()
            return

        dictionary = menu_context["dictionary"]

        title = "Dictionary from {} to {}.".format(
            dictionary.native_language,
            dictionary.translated_language)
        word_list = [str(current_word) for current_word in dictionary.words]
        dictionary_menu = consolemenu.SelectionMenu(
            word_list, title, exit_option_text="Up")

        dictionary_menu.show()
