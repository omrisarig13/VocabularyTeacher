"""
A base menu that will be used in the project.

File: menu.py
Description: This menu will be responsible on running the all the actions and
             interfacing with the user.
"""

import consolemenu


class Menu():
    """A menu that will handle all the interfaces with the user."""

    def __init__(self):
        """Initialize the object of the menu."""
        self._actions = {}
        self._context = {"actions": self._actions}
        self._menu = consolemenu.ConsoleMenu("Vocabulary Builder")

    def add_action(self, new_action, new_action_command):
        """Add a new action to the menu.

        :new_action: The new action to add to the menu.
        :new_action_command: The string that will run the command. It must be
                             a string that is not exists yet in the dictionary.
        :returns: None

        """
        if self._actions.get(new_action_command, None):
            raise KeyError("Command {} already exists in the menu.".format(
                new_action_command))

        self._actions[new_action_command] = new_action

        new_action_item = consolemenu.items.FunctionItem(
            new_action_command,
            new_action.run_command,
            kwargs={"menu_context": self._context})
        self._menu.append_item(new_action_item)

    def run(self):
        """Run the menu.

        This action will run the commands in the menu until a given command
        will raise ExitMenu. After this the menu will end.

        :returns: None

        """
        self._menu.show()
