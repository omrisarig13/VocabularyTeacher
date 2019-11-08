"""
Get the translate of the word to the learned language by the dictionary.

File: dictionary_learned_translate.py
"""

import menu
from Actions import menu_actions


class TranlateToLearnedDictionaryAction(menu_actions.BaseAction):
    """An action that prints the translations of a word to new languege."""

    COMMAND_NAME = "translate_to_learned_dictionary"
    HELP_TEXT = """
        Translate the word to the learned language using the dictionary.
        Get all the translations of the given word.
    """
    ARGUMENTS = """
            word_to_translate - The word to translate to the learned language.
    """
    USAGE = "{command_name} word_to_translate".format(
        command_name=COMMAND_NAME)

    def run_command(self, menu_context, *args, **kwargs):
        """Print all the translation of a given word.

        :menu_context: The context of the menu.
        :*args: The special arguments for the command. It will include the
                word to translate.
        :returns: True to make the menu continue to run

        """
        if len(args) != 1:
            raise menu.InvalidCommand(
                "Invalid number of arguments for command. Read the help")

        if menu_context.get("dictionary", None) is None:
            raise menu.InvalidCommand(
                "Can't translate without dictionary.")

        word_to_translate = args[0]
        dictionary = menu_context["dictionary"]

        print(dictionary.get_all_translations_to_translated_languege(
            word_to_translate))

        return True
