package com.vocabularyteacher.vocabularyteacher

import android.view.View
import android.widget.TextView
import androidx.constraintlayout.widget.ConstraintLayout

class DummyQuestion(
    val wordCouple: WordCouple,
    val dictionary: Dictionary)
{
    lateinit var questionLayout: ConstraintLayout
    lateinit var questionText: TextView

    fun setView(view: View) {
        this.questionLayout = view.findViewById(R.id.test_fragment_regular_question_layout)
        this.questionText = view.findViewById<TextView>(R.id.test_fragment_regular_question_question_text_view)

        this.questionText.text = "This is a dummy question.\nWhat is your Answer?"
        this.questionLayout.visibility = View.VISIBLE
    }

    fun endView() {
        this.questionLayout.visibility = View.GONE
    }
}

/*
interface Question {
    fun getAnswerFromWord(wordCouple: WordCouple): String

    fun getAnswer(questionWord: WordCouple): String {
        return this.getAnswerFromWord(questionWord)
    }

    fun getQuestionWord(wordCouple: WordCouple): String

    // TODO: Understand how to set the question with the view (probably pass a view to this function that will change).
    // fun getQuestion(TODO): TODO
    // fun checkAnswer(TODO): TODO
}
 */