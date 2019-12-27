package com.vocabularyteacher.vocabularyteacher


import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.EditText
import androidx.navigation.Navigation

/**
 * A simple [Fragment] subclass.
 */
class AddWord : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        super.onCreateView(inflater, container, savedInstanceState)
        val view = inflater.inflate(R.layout.fragment_add_word, container, false)

        view.findViewById<Button>(R.id.add_word_done_button).setOnClickListener {
            this.done_pressed(view)
        }
        return view
    }

    private fun done_pressed(view: View) {
        // Create a new word with all the variables from the form.
        val nativeWord = view.findViewById<EditText>(R.id.add_word_native_word_edit_text).text.toString()
        val translatedWord = view.findViewById<EditText>(R.id.add_word_translated_word_edit_text).text.toString()
        var knowledgeLevel = KnowledgeLevels.from(
            view.findViewById<EditText>(R.id.add_word_word_known_level_edit_text).text.toString().toInt())

        if (knowledgeLevel == null) {
            knowledgeLevel = KnowledgeLevels.UNKNOWN
        }

        // Add the new word to the dictionary.
        Dictionary.addWordCouple(WordCouple(nativeWord, translatedWord, knowledgeLevel!!))

        // Run the action that returns to the main menu.
        Navigation.findNavController(view).navigate(R.id.action_addWord_to_mainFragment)
    }
}
