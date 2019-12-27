package com.vocabularyteacher.vocabularyteacher


import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.TextView
import androidx.navigation.fragment.findNavController

/**
 * A simple [Fragment] subclass.
 */
class TestFragment : Fragment() {

    private val numberOfQuestionPerLevel: Int = 5
    private lateinit var currentQuestion: QuestionType
    private lateinit var checkButton: Button
    private lateinit var nextButton: Button
    private lateinit var questionTitle: TextView
    private lateinit var questionList: MutableList<WordCouple>
    private lateinit var fragmentView: View
    private var totalNumberOfQuestions: Int = 0
    private var numberQfQuestionsAsked: Int = 0
    private var numberOfRightAnswers: Int = 0

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        super.onCreateView(inflater, container, savedInstanceState)
        // Inflate the layout for this fragment
        val view = inflater.inflate(R.layout.fragment_test, container, false)

        this.checkButton = view.findViewById(R.id.test_fragment_check_button)
        this.nextButton = view.findViewById(R.id.test_fragment_next_button)
        this.questionTitle = view.findViewById(R.id.test_fragment_question_text_view)

        checkButton.setOnClickListener {
            this.endCurrentQuestion()
        }
        nextButton.setOnClickListener {
            this.getNextQuestion()
        }

        this.questionList = mutableListOf()
        for (knowledgeLevel in KnowledgeLevels.values()) {
            this.questionList.addAll(Dictionary.getRandomOrderedWordsFromLevel(knowledgeLevel).take(this.numberOfQuestionPerLevel))
        }
        this.totalNumberOfQuestions = this.questionList.size

        this.updateQuestionText()

        return view
    }

    private fun getNextQuestion() {
        // End the operation of the current question.
        this.currentQuestion.endView()
        this.numberQfQuestionsAsked++
        this.updateQuestionText()

        // Set the buttons so the user will be able to touch only the check button
        this.checkButton.visibility = View.VISIBLE
        this.nextButton.visibility = View.INVISIBLE

        // Set the next question.
        if (this.questionList.size > 0) {
            this.askNewQuestion()
        }
        else {
            this.findNavController().navigate(R.id.action_testFragment_to_testResultFragment)
        }
    }

    private fun updateQuestionText() {
        this.questionTitle.text = "Question (${this.numberQfQuestionsAsked+1} / ${this.totalNumberOfQuestions})"
    }

    private fun endCurrentQuestion() {
        if (when (this.currentQuestion.checkAnswer()) {
            QuestionAnswerTypes.RIGHT -> {
                this.currentQuestion.updateCorrectAnswer(context)
                this.numberOfRightAnswers++
                true
            }
            QuestionAnswerTypes.RIGHT_BUT_UNEXPECTED -> {
                this.currentQuestion.updateCorrectNotExpectedAnswer(context)
                false
            }
            QuestionAnswerTypes.WRONG -> {
                this.currentQuestion.updateWrongAnswer(context)
                true
            }
        }) {
            this.checkButton.visibility = View.INVISIBLE
            this.nextButton.visibility = View.VISIBLE
        }
    }

    private fun askNewQuestion() {
        this.currentQuestion = createQuestion(this.questionList.removeAt(0), Dictionary, this.fragmentView)
        this.currentQuestion.askQuestion()
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        this.fragmentView = view

        this.askNewQuestion()
    }
}
