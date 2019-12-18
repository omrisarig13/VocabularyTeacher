package com.example.vocabularyteacher

import android.content.Context
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Load the previous existing dictionary from the disk.
        this.openFileInput("dictionary").use {
            Dictionary.loadSerialized(it)
        }
    }


    override fun onStop() {
        super.onStop()

        // Write the dictionary file into the disk.
        this.openFileOutput("dictionary", Context.MODE_PRIVATE).use {
            Dictionary.serialize(it)
        }
    }
}
