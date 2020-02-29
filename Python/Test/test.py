"""
Implementation of a test in the project.

File: test.py
"""

import random

import word_couple
from Test.Question import question_factory


class Test():
    """A test that will check the knowledge level of the words."""

    DEFAULT_NUMBER_OF_QUESTIONS = 5

    def __init__(self, dictionary,
                 number_of_questions=DEFAULT_NUMBER_OF_QUESTIONS):
        """Initialize the object.

        :dictionary: The dictionary to use to get the words.
        :number_of_questions: The number of questions per knowledge level.

        """
        self._dictionary = dictionary
        self._number_of_questions = number_of_questions

    def _get_words_from_level(self, number_of_words, level, used_words):
        """Get some words from the given level.

        In case there won't be enough words, the function will return a word
        from a level below, or no word at all.

        :number_of_words: The number of words to get.
        :level: The level to get the words from.
        :used_words: Words already used in the test.
        :returns: A new list with the new words used.

        """
        all_words_in_level = self._dictionary.get_words_from_level(level)
        words = []

        while len(words) != number_of_words and all_words_in_level:
            current_word = random.choice(all_words_in_level)
            all_words_in_level.remove(current_word)

            if current_word not in used_words:
                words.append(current_word)

        if len(words) != number_of_words and level > 0:
            words.extend(self._get_words_from_level(
                (number_of_words - len(words)),
                level - 1,
                used_words + words))

        return words

    def _get_test_words(self):
        """Get all the words for the test.

        :returns: A list with all the words of the test.
        """
        used_words = []
        for current_level in range(word_couple.WordCouple.MAX_LEVEL + 1):
            used_words.extend(self._get_words_from_level(
                self._number_of_questions,
                current_level,
                used_words))
        return used_words

    def _get_test_questions(self):
        """Get all the questions for the test.

        :returns: A list with all the questions in the test.
        """
        words = self._get_test_words()
        current_question_factory = question_factory.QuestionFactory(
            self._dictionary)
        questions = []

        for current_word in words:
            questions.append(
                current_question_factory.get_question(current_word))

        return questions

    def run(self):
        """Run a test.

        :returns: None

        :note: The function will update the knowledge level of the words in the
               dictionary.
        """
        questions = self._get_test_questions()

        number_of_right_answers = 0

        for current_question in questions:
            answered_correctly = current_question.ask_question()
            if answered_correctly:
                number_of_right_answers += 1

        print("Answered correctly {}/{} questions".format(
            number_of_right_answers, len(questions)))
