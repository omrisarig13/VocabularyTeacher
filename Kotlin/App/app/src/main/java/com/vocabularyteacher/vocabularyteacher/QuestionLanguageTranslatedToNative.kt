package com.vocabularyteacher.vocabularyteacher

interface QuestionLanguageTranslatedToNative: QuestionLanguage {
    override fun getAnswerWord(wordCouple: WordCouple): String {
        return wordCouple.nativeWord
    }

    override fun getQuestionWord(wordCouple: WordCouple): String {
        return wordCouple.translatedWord
    }
}
