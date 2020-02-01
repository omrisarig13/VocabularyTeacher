"""
A module responsible on creating the right question.

The question will be determined according to the known level of the word in
question.

File: question_factory.py
"""

from Test.Question import translate_question
from Test.Question import multiple_choice_question


class QuestionFactory():
    """A class used to create different questions."""

    QUESTIONS_BY_LEVEL = {
        0: multiple_choice_question.MultipleChoiceToNativeQuestion,
        1: translate_question.TranslateToNativeQuestion,
        2: multiple_choice_question.MultipleChoiceToLearnedQuestion,
        3: translate_question.TranslateToLearnedQuestion,
        4: translate_question.TranslateToLearnedQuestion
    }

    def __init__(self, dictionary):
        """Initialize the question factory.

        :dictionary: The dictionary to use when creating questions.

        """
        self._dictionary = dictionary

    def get_question(self, word_for_question):
        """Get the appropriate question object for the current word.

        :word_for_question: The word for the question.
        :returns: The appropriate question. It will be one of the
                  implementation of AbstractQuestion class

        """
        word_level = word_for_question.word_known_level
        return self.QUESTIONS_BY_LEVEL[word_level](word_for_question,
                                                   self._dictionary)
