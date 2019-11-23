"""
Get the translate of the word to the native language by the dictionary.

File: dictionary_native_translate.py
"""

import qprompt

import menu
from Actions import menu_actions


class TranlateToNativeDictionaryAction(menu_actions.BaseAction):
    """An action that prints the translations of a word to native language."""

    COMMAND_NAME = "translate_to_native_dictionary"
    HELP_TEXT = """
        Translate the word to the native language using the dictionary.
        Get all the translations of the given word.
    """
    ARGUMENTS = """None"""
    USAGE = "{command_name}".format(command_name=COMMAND_NAME)

    def run_command(self, menu_context, *args, **kwargs):
        """Print all the translation of a given word.

        :menu_context: The context of the menu.
        :*args: The special arguments for the command. It will include the
                word to translate.
        :returns: True to make the menu continue to run

        """
        if menu_context.get("dictionary", None) is None:
            raise menu.InvalidCommand(
                "Can't translate without dictionary.")

        word_to_translate = qprompt.ask_str("Insert the word to translate")
        dictionary = menu_context["dictionary"]

        print(dictionary.get_all_translations_to_native(word_to_translate))

        qprompt.pause()
        return True
