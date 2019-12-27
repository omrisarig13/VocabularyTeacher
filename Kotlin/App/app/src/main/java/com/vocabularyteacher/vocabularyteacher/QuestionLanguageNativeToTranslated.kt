package com.vocabularyteacher.vocabularyteacher

interface QuestionLanguageNativeToTranslated: QuestionLanguage {
    override fun getAnswerWord(wordCouple: WordCouple): String {
        return wordCouple.translatedWord
    }

    override fun getQuestionWord(wordCouple: WordCouple): String {
        return wordCouple.nativeWord
    }
}