package com.vocabularyteacher.vocabularyteacher

import android.view.View
import android.view.ViewGroup
import android.widget.RadioButton
import android.widget.RadioGroup
import android.widget.TextView

class QuestionChoiceTranslatedToNative(
    override val wordCouple: WordCouple,
    override val dictionary: Dictionary,
    override val questionText: TextView,
    override val answersRadioGroup: RadioGroup,
    override val firstAnswer: RadioButton,
    override val secondAnswer: RadioButton,
    override val thirdAnswer: RadioButton,
    override val fourthAnswer: RadioButton,
    override val answerTextToUser: TextView,
    override val questionLayout: ViewGroup
) : QuestionLanguageTranslatedToNative, QuestionTypeChoices{

    constructor(wordCouple: WordCouple, dictionary: Dictionary, view: View) :
            this(
                wordCouple,
                dictionary,
                view.findViewById<TextView>(R.id.test_fragment_choice_question_question_text_view),
                view.findViewById<RadioGroup>(R.id.test_fragment_choice_question_answers_raido_gruop),
                view.findViewById<RadioButton>(R.id.test_fragment_choice_question_first_answer_radio_button),
                view.findViewById<RadioButton>(R.id.test_fragment_choice_question_second_answer_radio_button),
                view.findViewById<RadioButton>(R.id.test_fragment_choice_question_third_answer_radio_button),
                view.findViewById<RadioButton>(R.id.test_fragment_choice_question_fourth_answer_radio_button),
                view.findViewById<TextView>(R.id.test_fragment_choice_quesiton_answer_correctness_text_view),
                view.findViewById<ViewGroup>(R.id.test_fragment_choice_question_layout)
            )
}
