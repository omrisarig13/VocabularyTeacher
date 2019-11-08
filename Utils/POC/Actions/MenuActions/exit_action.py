"""
An action that will exit the menu.

File: exit_action.py
"""

from Actions import menu_actions


class ExitAction(menu_actions.BaseAction):
    """An action that will Exit the menu."""

    COMMAND_NAME = "exit"
    HELP_TEXT = "Exit the menu."
    ARGUMENTS = """None"""
    USAGE = "{command_name}".format(command_name=COMMAND_NAME)

    def run_command(self, menu_context, *args, **kwargs):
        """Run the command that will Exit the menu.

        :menu_context: The context of the menu.
        :*args: The special arguments for the command. Not used in this
                function.
        :returns: False, to make the menu stop.
        """
        return False
