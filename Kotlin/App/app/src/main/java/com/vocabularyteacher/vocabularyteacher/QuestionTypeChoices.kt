package com.vocabularyteacher.vocabularyteacher

import android.content.Context
import android.widget.RadioButton
import android.widget.RadioGroup
import android.widget.TextView

interface QuestionTypeChoices: QuestionType, QuestionLanguage {
    val wordCouple: WordCouple
    val dictionary: Dictionary
    val questionText: TextView
    val answersRadioGroup: RadioGroup
    val firstAnswer: RadioButton
    val secondAnswer: RadioButton
    val thirdAnswer: RadioButton
    val fourthAnswer: RadioButton
    val answerTextToUser: TextView

    override fun constructQuestion() {
        // Set the text of the question.
        val questionWord = this.getQuestionWord(this.wordCouple)
        this.questionText.text = "What is the translation of the word ${questionWord}?"

        // Get the answers and add them to the buttons
        val answersStrings: MutableList<String> = mutableListOf<String>()
        answersStrings.add(this.getAnswerWord(this.dictionary.wordList.random()))
        answersStrings.add(this.getAnswerWord(this.dictionary.wordList.random()))
        answersStrings.add(this.getAnswerWord(this.dictionary.wordList.random()))
        answersStrings.add(this.getAnswerWord(this.wordCouple))
        answersStrings.shuffle()
        this.firstAnswer.text = answersStrings[0]
        this.secondAnswer.text = answersStrings[1]
        this.thirdAnswer.text = answersStrings[2]
        this.fourthAnswer.text = answersStrings[3]
    }

    override fun checkAnswer(): QuestionAnswerTypes {
        val userAnswer = when (this.answersRadioGroup.checkedRadioButtonId) {
            this.firstAnswer.id -> this.firstAnswer.text.toString()
            this.secondAnswer.id -> this.secondAnswer.text.toString()
            this.thirdAnswer.id -> this.thirdAnswer.text.toString()
            else -> this.fourthAnswer.text.toString()
        }
        return this.checkAnswerWord(userAnswer, this.wordCouple, this.dictionary)
    }

    override fun updateCorrectAnswer(context: Context?) {
        this.wordCouple.userAnsweredCorrectly()
        this.answerTextToUser.text = "Well done! You answered correctly."
        // TODO: To refactor this ugly mess
        val userAnswer = when (this.answersRadioGroup.checkedRadioButtonId) {
            this.firstAnswer.id -> this.firstAnswer
            this.secondAnswer.id -> this.secondAnswer
            this.thirdAnswer.id -> this.thirdAnswer
            else -> this.fourthAnswer
        }
        userAnswer.setBackgroundResource(android.R.color.holo_green_dark)
    }

    override fun updateWrongAnswer(context: Context?) {
        this.wordCouple.userAnsweredWrong()
        this.answerTextToUser.text = "Wrong Answer!"
        // TODO: To refactor this ugly mess
        val userAnswer = when (this.answersRadioGroup.checkedRadioButtonId) {
            this.firstAnswer.id -> this.firstAnswer
            this.secondAnswer.id -> this.secondAnswer
            this.thirdAnswer.id -> this.thirdAnswer
            else -> this.fourthAnswer
        }
        // TODO: To refactor this ugly mess
        userAnswer.setBackgroundResource(android.R.color.holo_red_dark)
        val correctAnswer = when (this.getAnswerWord(this.wordCouple)) {
            this.firstAnswer.text -> this.firstAnswer
            this.secondAnswer.text -> this.secondAnswer
            this.thirdAnswer.text -> this.thirdAnswer
            else -> this.fourthAnswer
        }
        correctAnswer.setBackgroundResource(android.R.color.holo_green_dark)
    }

    override fun endView() {
        super.endView()
        this.firstAnswer.setBackgroundResource(android.R.color.white)
        this.secondAnswer.setBackgroundResource(android.R.color.white)
        this.thirdAnswer.setBackgroundResource(android.R.color.white)
        this.fourthAnswer.setBackgroundResource(android.R.color.white)
        this.answerTextToUser.text = ""
    }
}