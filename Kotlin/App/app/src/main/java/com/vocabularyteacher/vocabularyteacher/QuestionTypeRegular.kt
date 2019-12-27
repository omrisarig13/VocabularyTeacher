package com.vocabularyteacher.vocabularyteacher

import android.content.Context
import android.widget.EditText
import android.widget.TextView

interface QuestionTypeRegular: QuestionType, QuestionLanguage {
    val wordCouple: WordCouple
    val dictionary: Dictionary
    val questionText: TextView
    val answerText: EditText
    val correctAnswer: TextView

    override fun constructQuestion() {
        val questionWord = this.getQuestionWord(this.wordCouple)
        val question = "What is the translation of the word ${questionWord}?"

        this.questionText.text = question
    }

    override fun checkAnswer(): QuestionAnswerTypes {
        val userAnswer = this.answerText.text.toString()
        return this.checkAnswerWord(userAnswer, this.wordCouple, this.dictionary)
    }

    override fun updateCorrectAnswer(context: Context?) {
        this.wordCouple.userAnsweredCorrectly()
        this.correctAnswer.text = "Well done! You answered correctly."
    }

    override fun updateWrongAnswer(context: Context?) {
        this.wordCouple.userAnsweredWrong()
        this.correctAnswer.text = "Wrong Answer!\nThe correct answer is ${this.getAnswerWord(this.wordCouple)}"
    }

    override fun endView() {
        super.endView()
        this.correctAnswer.text = ""
    }
}