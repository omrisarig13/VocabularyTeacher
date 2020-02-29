"""
An implementation of translate questions.

File: translate_question.py
"""

import qprompt

from Test.Question import abstract_question
from Utils import safe_ask


class TranslateQuestion(abstract_question.AbstractQuestion):
    """Implement a translate question."""

    QUESTION_FORMAT = "What is the translation of the word {}?"

    def _get_question(self):
        """Get the string representing the question.

        :returns: A string with the question.

        """
        return self.QUESTION_FORMAT.format(self._get_question_word())

    def _get_answer_from_user(self):
        """Get the answer from the user.

        :returns: The string with the answer from the user.

        """
        return safe_ask.safe_ask(qprompt.ask_str, "Answer")


class TranslateToNativeQuestion(TranslateQuestion):
    """A translate question from learned language to native language."""

    def _check_answer(self, current_answer):
        """Check the current answer got.

        :current_answer: The answer got from the user.
        :returns: One of the optional answers in this module (RIGHT_ANSWER,
                  WRONG_ANSWER, RIGHT_ANSWER_BUT_NOT_WANTED)

        """
        return self._check_native_word_answer(current_answer)

    def _get_question_word(self):
        """Get the word of the question.

        :returns: Get the word the question is about.

        """
        return self._current_word.translated_word.get_most_common_spelling()

    def _get_answer_from_word(self, current_word):
        """Get the answer from the current word.

        :current_word: The word to get the answer from.
        :returns: A string containing the answer from the word.

        """
        return current_word.native_word.get_most_common_spelling()


class TranslateToLearnedQuestion(TranslateQuestion):
    """A translate question from native language to learned language."""

    def _check_answer(self, current_answer):
        """Check the current answer got.

        :current_answer: The answer got from the user.
        :returns: One of the optional answers in this module (RIGHT_ANSWER,
                  WRONG_ANSWER, RIGHT_ANSWER_BUT_NOT_WANTED)

        """
        return self._check_translated_word_answer(current_answer)

    def _get_question_word(self):
        """Get the word of the question.

        :returns: Get the word the question is about.

        """
        return self._current_word.native_word.get_most_common_spelling()


    def _get_answer_from_word(self, current_word):
        """Get the answer from the current word.

        :current_word: The word to get the answer from.
        :returns: A string containing the answer from the word.

        """
        return current_word.translated_word.get_most_common_spelling()
