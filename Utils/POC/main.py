"""
The main module of the project.

File: main.py
Description: Add all the commands to the menu of the project, than run the
             menu.
"""

import menu
from Actions.MenuActions import help_action
from Actions.MenuActions import exit_action
from Actions.ProjectActions import add_dictionary
from Actions.ProjectActions import add_new_word
from Actions.ProjectActions import load_dictionary
from Actions.ProjectActions import print_dictionary
from Actions.ProjectActions import save_dictionary

ALL_AVAILABLE_COMMANDS = [
    help_action.HelpAction,
    exit_action.ExitAction,
    add_dictionary.AddDictionaryAction,
    add_new_word.AddNewWordAction,
    load_dictionary.LoadDictionaryAction,
    print_dictionary.PrintDictionaryAction,
    save_dictionary.SaveDictionaryAction
]


def main():
    """Run the menu.

    This is the main function of the project.

    :returns: None

    """
    menu_object = menu.Menu()

    for current_class in ALL_AVAILABLE_COMMANDS:
        current_object = current_class()
        current_object.register_command(menu_object)

    menu_object.run()


if __name__ == '__main__':
    main()
