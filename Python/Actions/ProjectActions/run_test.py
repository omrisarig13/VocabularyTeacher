"""
An action that will run a test on the words in the dictionary.

File: run_test.py
"""

import qprompt

from Actions import menu_actions
from Test import test
from Utils import safe_ask


class RunTestAction(menu_actions.BaseAction):
    """An action that will Run a test on the words in the dictionary."""

    COMMAND_NAME = "Run Test"
    HELP_TEXT = "Run a test on the words in the dictionary."

    def run_command(self, menu_context):
        """Run the command that will add the new word to the dictionary.

        :menu_context: The context of the menu.

        """
        dictionary = menu_context.get("dictionary", None)
        if dictionary is None:
            print("Menu does not have a dictionary")
            qprompt.pause()
            return

        number_of_questions = safe_ask.safe_ask(
            qprompt.ask_int,
            "Insert the number of questions per known level",
            test.Test.DEFAULT_NUMBER_OF_QUESTIONS,
            vld=lambda x: x > 0)

        current_test = test.Test(dictionary, number_of_questions)

        current_test.run()

        qprompt.pause()
