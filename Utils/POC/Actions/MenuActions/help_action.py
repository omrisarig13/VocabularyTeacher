"""
An action that will print the help of the menu.

File: help_action.py
"""

import consolemenu
import qprompt

from Actions import menu_actions


class HelpAction(menu_actions.BaseAction):
    """An action that will print the help of the menu."""

    COMMAND_NAME = "Help"
    HELP_TEXT = "Print this help."

    @staticmethod
    def _run_help_on_command(menu_context, command_string):
        """Run the help on the given command.

        :menu_context: The context of the menu.
        :command_string: The name of the command.
        :returns: None

        """
        # Print the help on the specific command.
        command = menu_context["actions"].get(command_string, None)
        print(command.get_help())
        qprompt.pause()

    def run_command(self, menu_context):
        """Run the command that will print the help of the menu.

        :menu_context: The context of the menu.

        :Note: The function prints the dictionary to the user.
        """
        menu = consolemenu.ConsoleMenu("help menu", exit_option_text="up")

        for command in menu_context["actions"].keys():
            menu.append_item(
                consolemenu.items.FunctionItem(
                    command + " command",
                    self._run_help_on_command,
                    kwargs={
                        "menu_context": menu_context,
                        "command_string": command},
                    should_exit=False))

        menu.show(True)
