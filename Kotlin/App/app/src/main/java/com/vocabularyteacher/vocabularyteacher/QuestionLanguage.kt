package com.vocabularyteacher.vocabularyteacher

interface QuestionLanguage {
    // Get the answer from the word
    fun getAnswerWord(wordCouple: WordCouple): String

    // Get the word of the question from the word couple
    fun getQuestionWord(wordCouple: WordCouple): String

    // Check if the given answer one of the right answers
    fun checkAnswerWord(answer: String, wordCouple: WordCouple, dictionary: Dictionary): QuestionAnswerTypes {
        if (answer == this.getAnswerWord(wordCouple)) {
            return QuestionAnswerTypes.RIGHT
        }

        for (currentWordCouple in dictionary.wordList) {
            if (answer == this.getAnswerWord(currentWordCouple) &&
                this.getQuestionWord(wordCouple) == this.getQuestionWord(currentWordCouple)
            ) {
                return QuestionAnswerTypes.RIGHT_BUT_UNEXPECTED
            }
        }

        return QuestionAnswerTypes.WRONG
    }
}