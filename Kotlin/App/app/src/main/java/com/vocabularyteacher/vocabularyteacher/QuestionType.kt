package com.vocabularyteacher.vocabularyteacher

import android.content.Context
import android.view.View
import android.view.ViewGroup
import android.widget.Toast

interface QuestionType {
    val questionLayout: ViewGroup

    // Set the view of the fragment, with the wanted view for the question.
    fun setView() {
        this.questionLayout.visibility = View.VISIBLE
    }

    // End the view of the question, making it disappear from the screen.
    fun endView() {
        this.questionLayout.visibility = View.GONE
    }

    // Check the answer according to the value that the user has entered.
    fun checkAnswer(): QuestionAnswerTypes

    // Construct the question from the dictionary and the word for the question.
    fun constructQuestion()

    fun askQuestion() {
        this.constructQuestion()
        this.setView()
    }

    // Update the screen when the result from the user was the correct result.
    fun updateCorrectAnswer(context: Context?)

    // Update the screen when the result from the user was wrong.
    fun updateWrongAnswer(context: Context?)

    // Update the screen when the result from the user was correct but not the expected ones.
    fun updateCorrectNotExpectedAnswer(context: Context?) {
        Toast.makeText(
            context,
            "The answer is right but not the expected one.\nTry again!",
            Toast.LENGTH_LONG).show()
    }
}
