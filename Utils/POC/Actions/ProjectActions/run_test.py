"""
An action that will run a test on the words in the dictionary.

File: run_test.py
"""

import qprompt

from Actions import menu_actions
from Test import test


class RunTestAction(menu_actions.BaseAction):
    """An action that will Run a test on the words in the dictionary."""

    COMMAND_NAME = "run_test"
    HELP_TEXT = "Run a test on the words in the dictionary."
    ARGUMENTS = """
            number_of_words_per_level - optional - the number of words in every
                                                   level for the test.
    """
    USAGE = "{command_name} [number_of_words_per_level]".format(
        command_name=COMMAND_NAME)

    def run_command(self, menu_context, *args, **kwargs):
        """Run the command that will add the new word to the dictionary.

        :menu_context: The context of the menu.
        :*args: The special arguments for the command. It might include the
                number of words per level for the test.
        :returns: True to make the menu continue to run

        """
        if menu_context.get("dictionary", None) is None:
            print("Menu does not have a dictionary")
            qprompt.pause()
            return True

        dictionary = menu_context["dictionary"]

        if len(args) == 2:
            current_test = test.Test(dictionary, int(args[1]))
        else:
            current_test = test.Test(dictionary)

        current_test.run()

        qprompt.pause()

        return True
