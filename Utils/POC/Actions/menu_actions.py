"""
Actions that will be in the menu and run as part of it.

File: menu_actions.py
Description: This module contains the abstract implementation of an action in
             the project.
"""

import abc


class BaseAction(abc.ABC):
    """A base action.

    This action is an abstract class, all the other actions will inherit this
    action and implement its functions in their own way.
    """

    HELP_FORMAT = """        Name: {command_name}
        USAGE: {usage}

        Help: {help_message}

        Arguments: {arguments}
    """

    def __init__(self):
        """Initialize the action object.

        :command_name: The name of the action command.
        :help_message: The help message of the command.
        :returns: None

        """
        self._command_name = self.COMMAND_NAME
        self._help_message = self.format_help_message(self.COMMAND_NAME,
                                                      self.USAGE,
                                                      self.HELP_TEXT,
                                                      self.ARGUMENTS)
        super().__init__()

    def register_command(self, menu):
        """Register the command to the menu.

        :menu: The menu object to register the command into.
        :returns: None

        """
        menu.add_action(self, self._command_name)

    @staticmethod
    def format_help_message(command_name, usage, help_message, arguments):
        """Format the help message with a constant format.

        :command_name: The name of the command.
        :usage: The usage of the command.
        :help_message: The help description of the command.
        :arguments: The arguments that the command can get.
        :returns: The formatted help message.

        """
        return BaseAction.HELP_FORMAT.format(command_name=command_name,
                                             usage=usage,
                                             help_message=help_message,
                                             arguments=arguments)

    def get_help(self):
        """Get the help on the current command.

        :returns: The help on the current command.

        """
        return self._help_message

    @abc.abstractmethod
    def run_command(self, menu_context, *args, **kwargs):
        """Run the given command.

        :menu_context: The context of the menu. This will be a dictionary with
                       all the objects that is saved in the menu, that needs to
                       save and be processed in different actions. The action
                       can read its data and update it as it wants.
        :returns: True to make the menu continue running, False to make the
                  menu stop.

        :note: Any specific parameters to the command will be passed through
               args and kwargs arguments.

        """
