"""
An implementation of multiple choice questions.

File: multiple_choice_question.py
"""

import random
import abc

import qprompt

from Test.Question import abstract_question
from Utils import safe_ask


class MultipleChoiceQuestion(abstract_question.AbstractQuestion):
    """Implement a multiple choice question."""

    NUMBER_OF_ANSWERS = 4
    QUESTION_FORMAT = """
        What is the translation of the word "{}"?
        Possible answers:
            1. {}\t2. {}
            3. {}\t4. {}
    """

    def _get_answers_from_words(self, word_couples):
        """Get the actual answers from the word couples.

        :word_couples: A list of all the word couples to extract the answers
                       from.
        :returns: A list with the same length as the word couples, containing
                  only the answers themselves.
        """
        answers = []
        for current_word_couple in word_couples:
            answers.append(self._get_answer_from_word(current_word_couple))

        return answers

    def _get_answers(self):
        """Get all the possible answers for the question.

        :returns: A list with three possible answers for the question.

        """
        word_couples = []
        for _ in range(self.NUMBER_OF_ANSWERS - 1):
            current_word_couple = self._current_word
            while current_word_couple == self._current_word:
                current_word_couple = random.choice(self._dictionary.words)
            word_couples.append(current_word_couple)

        return self._get_answers_from_words(word_couples)

    def __init__(self, current_word, dictionary):
        """Initialize the object with all its needed fields."""
        abstract_question.AbstractQuestion.__init__(
            self,
            current_word,
            dictionary)
        self._all_answers = (
            self._get_answers() +
            [self._get_answer()])
        random.shuffle(self._all_answers)

    def _get_question(self):
        """Get the string representing the question.

        :returns: A string with the question.

        """
        return self.QUESTION_FORMAT.format(self._get_question_word(),
                                           self._all_answers[0],
                                           self._all_answers[1],
                                           self._all_answers[2],
                                           self._all_answers[3])

    @abc.abstractmethod
    def _check_answer_word(self, answer_word):
        """Check if the current word is the correct answer.

        :answer_word: The answer got from the user.
        :returns: One of the optional answers in this module (RIGHT_ANSWER,
                  WRONG_ANSWER, RIGHT_ANSWER_BUT_NOT_WANTED)

        """

    def _check_answer(self, current_answer):
        """Check the current answer got.

        :current_answer: The answer got from the user.
        :returns: One of the optional answers in this module (RIGHT_ANSWER,
                  WRONG_ANSWER, RIGHT_ANSWER_BUT_NOT_WANTED)

        """
        # -1 is to make the answer zero based
        answer_word = self._all_answers[int(current_answer)-1]
        return self._check_answer_word(answer_word)

    def _get_answer_from_user(self):
        """Get the answer from the user.

        :returns: The number of the answer.

        """
        return safe_ask.safe_ask(qprompt.ask_int, "Answer", vld=range(1, 5))


class MultipleChoiceToNativeQuestion(MultipleChoiceQuestion):
    """A multiple choice question from learned language to native language."""

    def _check_answer_word(self, answer_word):
        """Check if the current word is the correct answer.

        :answer_word: The answer got from the user.
        :returns: One of the optional answers in this module (RIGHT_ANSWER,
                  WRONG_ANSWER, RIGHT_ANSWER_BUT_NOT_WANTED)

        """
        return self._check_native_word_answer(answer_word)

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


class MultipleChoiceToLearnedQuestion(MultipleChoiceQuestion):
    """A multiple choice question from native language to learned language."""

    def _check_answer_word(self, answer_word):
        """Check if the current word is the correct answer.

        :answer_word: The answer got from the user.
        :returns: One of the optional answers in this module (RIGHT_ANSWER,
                  WRONG_ANSWER, RIGHT_ANSWER_BUT_NOT_WANTED)

        """
        return self._check_translated_word_answer(answer_word)

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
