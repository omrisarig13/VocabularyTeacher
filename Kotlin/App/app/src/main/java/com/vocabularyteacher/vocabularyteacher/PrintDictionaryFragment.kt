package com.vocabularyteacher.vocabularyteacher


import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView

/**
 * A simple [Fragment] subclass.
 */
class PrintDictionaryFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        super.onCreateView(inflater, container, savedInstanceState)
        // Inflate the layout for this fragment
        val view = inflater.inflate(R.layout.fragment_print_dictionary, container, false)

        // Create a long string with all the words
        var allWords: String = ""
        for (wordCouple in Dictionary.wordList) {
            allWords = allWords + wordCouple.toString() + "\n"
        }

        // Print all the words to the screen
        view.findViewById<TextView>(R.id.print_dictionary_words_text_view).text = allWords

        return view
    }


}
