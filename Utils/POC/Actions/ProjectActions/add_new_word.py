"""
An action that will add a new word pair to the dictionary.

File: add_new_word.py
"""

import word_couple

from Actions import menu_actions
import menu


class AddNewWordAction(menu_actions.BaseAction):
    """An action that will Add a new word to the dictionary."""

    COMMAND_NAME = "add_new_word"
    HELP_TEXT = "Add the given new word to the dictionary."
    ARGUMENTS = """
            native_word - The word in the native language.
            learned_word - The word in the learned language.
            known_level - optional - a number representing the word known
                                     level.
    """
    USAGE = "{command_name} native_word learned_word [known_level]".format(
        command_name=COMMAND_NAME)

    def run_command(self, menu_context, *args, **kwargs):
        """Run the command that will add the new word to the dictionary.

        :menu_context: The context of the menu to add the dictionary to.
        :*args: The special arguments for the command. It will include the
                new word in the native language, the new word in the learned
                language and maybe the known level of the word.
        :returns: True to make the menu continue to run

        :Note: This functions adds the new word to the dictionary.

        """
        if len(args) == 3:
            known_level = args[2]
        elif len(args) == 2:
            known_level = 0
        else:
            raise menu.InvalidCommand(
                "Invalid number of arguments for command. Read the help")

        if menu_context.get("dictionary", None) is None:
            raise menu.InvalidCommand("Menu does not have a dictionary")

        native_word = args[0]
        learned_word = args[1]

        new_word = word_couple.WordCouple(native_word, learned_word,
                                          known_level)
        menu_context["dictionary"].add_word(new_word)

        return True
