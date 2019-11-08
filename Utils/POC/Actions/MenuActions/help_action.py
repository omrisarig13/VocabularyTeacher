"""
An action that will print the help of the menu.

File: help_action.py
"""

import menu
from Actions import menu_actions


class HelpAction(menu_actions.BaseAction):
    """An action that will print the help of the menu."""

    COMMAND_NAME = "help"
    HELP_TEXT = "Print this help."
    ARGUMENTS = """None"""
    USAGE = "{command_name}".format(command_name=COMMAND_NAME)

    def run_command(self, menu_context, *args, **kwargs):
        """Run the command that will print the help of the menu.

        :menu_context: The context of the menu.
        :*args: The special arguments for the command. In case there will be
                a command name in it the help of the command will be
                printed. Otherwise, the general help will be printed.
        :returns: True to make the menu continue running.

        :Note: The function prints the dictionary to the user.
        """
        if not args:
            # Print the help on all the commands.
            print("Those are the available commands in the menu:")
            for current_command in menu_context["actions"].keys():
                print("\t{}".format(current_command))

            print("Run help <command_name> to get the help of any command")
        elif len(args) == 1:
            # Print the help on the specific command.
            command_string = args[0]
            command = menu_context["actions"].get(command_string, None)
            if command is None:
                raise menu.InvalidCommand("Got invalid command for help.")
            print(command.get_help())
        else:
            # Invalid number of arguments.
            raise menu.InvalidCommand(
                "Invalid number of arguments for command. Read the help")

        return True
