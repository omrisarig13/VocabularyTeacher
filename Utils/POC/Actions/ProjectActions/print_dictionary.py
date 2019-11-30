"""
An action that will print the dictionary to the user.

File: print_dictionary.py
"""

import consolemenu
import qprompt

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
            print("Menu does not have a dictionary")
            qprompt.pause()
            return True

        dictionary = menu_context["dictionary"]

        title = "Dictionary from {} to {}.".format(
            dictionary.native_language,
            dictionary.translated_language)
        word_list = [str(current_word) for current_word in dictionary.words]
        dictionary_menu = consolemenu.SelectionMenu(
            word_list, title, exit_option_text="Up")

        dictionary_menu.show()

        return True
