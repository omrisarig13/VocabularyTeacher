"""
The implementation of an abstract question in the project.

File: abstract_question.py
"""

import abc


class AbstractQuestion(abc.ABC):
    """Implement an abstract class of question."""

    RIGHT_ANSWER = 0
    WRONG_ANSWER = 1
    RIGHT_ANSWER_BUT_NOT_WANTED = 2

    @abc.abstractmethod
    def _get_answer_from_word(self, current_word):
        """Get the answer from the current word.

        :current_word: The word to get the answer from.
        :returns: A string containing the answer from the word.

        """

    def _get_answer(self):
        """Get the right answer for the question.

        :returns: The right answer for the question

        """
        return self._get_answer_from_word(self._current_word)

    @abc.abstractmethod
    def _get_question_word(self):
        """Get the word of the question.

        :returns: Get the word the question is about.

        """

    def __init__(self, current_word, dictionary):
        """Initialize the object with all its needed fields."""
        abc.ABC.__init__(self)
        self._current_word = current_word
        self._dictionary = dictionary
        self._right_answer = self._get_answer()

    @abc.abstractmethod
    def _get_question(self):
        """Get the string representing the question.

        :returns: A string with the question.

        """

    @abc.abstractmethod
    def _check_answer(self, current_answer):
        """Check the current answer got.

        :current_answer: The answer got from the user.
        :returns: One of the optional answers in this module (RIGHT_ANSWER,
                  WRONG_ANSWER, RIGHT_ANSWER_BUT_NOT_WANTED)

        """

    @abc.abstractmethod
    def _get_answer_from_user(self):
        """Get the answer from the user.

        :returns: The answer got from the user.

        """

    def ask_question(self):
        """Ask the user the current question.

        :returns: True if the user has answered right, False otherwise.

        :note: The question will update the word pair with the result.

        """
        # Print the question.
        question = self._get_question()
        print(question)

        # Get answers until getting the right answer or a wrong answer.
        answer = self._get_answer_from_user()
        current_answer_correctness = self._check_answer(answer)
        while current_answer_correctness == self.RIGHT_ANSWER_BUT_NOT_WANTED:
            print("Your answer is correct but not the wanted one. Try again.")
            answer = self._get_answer_from_user()
            current_answer_correctness = self._check_answer(answer)

        # Update the number of answers for the question and return the result.
        if current_answer_correctness == self.RIGHT_ANSWER:
            print("Correct answer!")
            self._current_word.answered_right()
            return True

        print('Wrong answer! Correct one is "{}"'.format(self._get_answer()))
        self._current_word.answered_wrong()
        return False

    def _check_native_word_answer(self, answer):
        """Check if the answer is the right native word of the question.

        :answer: The answer got from the user.
        :returns: One of the optional answers in this module (RIGHT_ANSWER,
                  WRONG_ANSWER, RIGHT_ANSWER_BUT_NOT_WANTED)

        """
        if self._current_word.native_word.is_same_word(answer):
            return self.RIGHT_ANSWER

        all_translations = self._dictionary.get_all_translations_to_native(
            self._current_word.translated_word.get_all_word_spellings())

        if answer in all_translations:
            return self.RIGHT_ANSWER_BUT_NOT_WANTED

        return self.WRONG_ANSWER

    def _check_translated_word_answer(self, answer):
        """Check if the answer is the right translated word of the question.

        :answer: The answer got from the user.
        :returns: One of the optional answers in this module (RIGHT_ANSWER,
                  WRONG_ANSWER, RIGHT_ANSWER_BUT_NOT_WANTED)

        """
        if self._current_word.translated_word.is_same_word(answer):
            return self.RIGHT_ANSWER

        all_translations = self._dictionary.get_all_translations_to_learned(
            self._current_word.native_word.get_all_word_spellings())

        if answer in all_translations:
            return self.RIGHT_ANSWER_BUT_NOT_WANTED

        return self.WRONG_ANSWER
