"""
The main module of the project.

File: main.py
Description: Add all the commands to the menu of the project, than run the
             menu.
"""

import menu
from Actions.MenuActions import help_action
from Actions.ProjectActions import add_dictionary
from Actions.ProjectActions import add_new_word
from Actions.ProjectActions import add_new_words_from_file
from Actions.ProjectActions import load_dictionary
from Actions.ProjectActions import print_dictionary
from Actions.ProjectActions import save_dictionary
from Actions.ProjectActions import extend_dictionary
from Actions.ProjectActions import dictionary_learned_translate
from Actions.ProjectActions import dictionary_native_translate
from Actions.ProjectActions import run_test
from Actions.ProjectActions import print_summary
from Actions.ProjectActions import delete_word

ALL_AVAILABLE_COMMANDS = [
    load_dictionary.LoadDictionaryAction,
    add_dictionary.AddDictionaryAction,
    save_dictionary.SaveDictionaryAction,
    print_dictionary.PrintDictionaryAction,
    print_summary.PrintSummaryAction,
    run_test.RunTestAction,
    add_new_word.AddNewWordAction,
    add_new_word.BulkAddNewWordAction,
    add_new_words_from_file.AddNewWordsFromFileAction,
    extend_dictionary.ExtendDictionaryAction,
    dictionary_learned_translate.TranlateToLearnedDictionaryAction,
    dictionary_native_translate.TranlateToNativeDictionaryAction,
    delete_word.DeleteWordAction,
    help_action.HelpAction,
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
