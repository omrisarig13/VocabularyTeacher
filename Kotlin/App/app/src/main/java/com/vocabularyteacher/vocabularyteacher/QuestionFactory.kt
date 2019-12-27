package com.vocabularyteacher.vocabularyteacher

import android.view.View

// Create the question for the given word couple
fun createQuestion(wordCouple: WordCouple, dictionary: Dictionary, view: View): QuestionType {
    return when (wordCouple.knownLevel) {
        KnowledgeLevels.UNKNOWN -> QuestionChoiceTranslatedToNative(wordCouple, dictionary, view)
        KnowledgeLevels.INEXPERIENCE -> QuestionRegularTranslatedToNative(wordCouple, dictionary, view)
        KnowledgeLevels.MEDIUM -> QuestionChoiceNativeToTranslated(wordCouple, dictionary, view)
        KnowledgeLevels.EXPERIENCED -> QuestionRegularNativeToTranslated(wordCouple, dictionary, view)
        KnowledgeLevels.KNOWN -> QuestionRegularNativeToTranslated(wordCouple, dictionary, view)
    }
}
