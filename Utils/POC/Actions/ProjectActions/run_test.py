"""
An action that will run a test on the words in the dictionary.

File: run_test.py
"""

import qprompt

from Actions import menu_actions
from Test import test


class RunTestAction(menu_actions.BaseAction):
    """An action that will Run a test on the words in the dictionary."""

    COMMAND_NAME = "Run Test"
    HELP_TEXT = "Run a test on the words in the dictionary."

    def run_command(self, menu_context):
        """Run the command that will add the new word to the dictionary.

        :menu_context: The context of the menu.

        """
        if menu_context.get("dictionary", None) is None:
            print("Menu does not have a dictionary")
            qprompt.pause()
            return

        dictionary = menu_context["dictionary"]

        current_test = test.Test(dictionary)

        current_test.run()

        qprompt.pause()
