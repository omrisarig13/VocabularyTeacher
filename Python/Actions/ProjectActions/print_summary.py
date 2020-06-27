"""
An action that will print a summary about the current dictionary.

File: print_summary.py
"""

import qprompt

import dictionary

from Actions import menu_actions


class PrintSummaryAction(menu_actions.BaseAction):
    """An action that will print the summary of the current dictionary."""

    COMMAND_NAME = "Print Summary"
    HELP_TEXT = "Print a summary of all the words in the dictionary."

    def run_command(self, menu_context):
        """Run the command that will print a summary of the dictionary.

        :menu_context: The context of the menu.

        """
        dictionary = menu_context.get("dictionary", None)
        if dictionary is None:
            print("Menu does not have a dictionary")
            qprompt.pause()
            return

        dictionary.print_summary()

        qprompt.pause()
