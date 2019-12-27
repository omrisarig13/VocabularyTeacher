package com.vocabularyteacher.vocabularyteacher

import android.view.View
import android.view.ViewGroup
import android.widget.EditText
import android.widget.TextView

class QuestionRegularNativeToTranslated(
    override val wordCouple: WordCouple,
    override val dictionary: Dictionary,
    override val questionText: TextView,
    override val answerText: EditText,
    override val correctAnswer: TextView,
    override val questionLayout: ViewGroup
) : QuestionLanguageNativeToTranslated, QuestionTypeRegular {
    constructor(wordCouple: WordCouple, dictionary: Dictionary, view: View) :
            this(
                wordCouple,
                dictionary,
                view.findViewById<TextView>(R.id.test_fragment_regular_question_question_text_view),
                view.findViewById<EditText>(R.id.test_fragment_regular_question_answer_edit_text),
                view.findViewById<TextView>(R.id.test_fragment_regular_question_correct_answer_text_view),
                view.findViewById<ViewGroup>(R.id.test_fragment_regular_question_layout)
            )
}