"""
Get the translate of the word to the learned language by the dictionary.

File: dictionary_learned_translate.py
"""

import qprompt

from Actions import menu_actions
from Utils import safe_ask


class TranlateToLearnedDictionaryAction(menu_actions.BaseAction):
    """An action that prints the translations of a word to new language."""

    COMMAND_NAME = "Translate To learned Language"
    HELP_TEXT = """
        Translate the word to the learned language using the dictionary.
        Get all the translations of the given word.
    """

    def run_command(self, menu_context):
        """Print all the translation of a given word.

        :menu_context: The context of the menu.
        :*args: The special arguments for the command. It will include the
                word to translate.

        """
        if menu_context.get("dictionary", None) is None:
            print("Can't translate without dictionary.")
            qprompt.pause()
            return

        word_to_translate = safe_ask.safe_ask(
            qprompt.ask_str,
            "Insert the word to translate")
        dictionary = menu_context["dictionary"]

        print(dictionary.get_all_translations_to_learned(
            [word_to_translate]))
        qprompt.pause()
