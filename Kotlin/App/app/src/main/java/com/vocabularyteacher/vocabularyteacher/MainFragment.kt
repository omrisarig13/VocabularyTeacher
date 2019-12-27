package com.vocabularyteacher.vocabularyteacher


import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.navigation.Navigation

/**
 * A simple [Fragment] subclass.
 */
class MainFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        super.onCreateView(inflater, container, savedInstanceState)
        // Inflate the layout for this fragment
        val view = inflater.inflate(R.layout.fragment_main, container, false)

        view.findViewById<Button>(R.id.main_run_test_button).setOnClickListener(
            Navigation.createNavigateOnClickListener(R.id.action_mainFragment_to_testFragment))
        view.findViewById<Button>(R.id.main_add_word_button).setOnClickListener(
            Navigation.createNavigateOnClickListener(R.id.action_mainFragment_to_addWord))
        view.findViewById<Button>(R.id.main_print_dictionary_button).setOnClickListener(
            Navigation.createNavigateOnClickListener(R.id.action_mainFragment_to_printDictionaryFragment))
        view.findViewById<Button>(R.id.main_clear_dictionary).setOnClickListener {
            Dictionary.clearDictionary()
        }

        return view
    }


}
