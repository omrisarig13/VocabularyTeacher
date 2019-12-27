package com.vocabularyteacher.vocabularyteacher

import android.content.Context
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.navigation.findNavController
import androidx.navigation.ui.NavigationUI

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Load the previous existing dictionary from the disk.
        val previousDictionary = try {this.openFileInput("dictionary") } catch (e: java.io.FileNotFoundException) { null }
        previousDictionary?.use {
            Dictionary.loadSerialized(it)
        }

        // Set the back button.
        val navController = this.findNavController(R.id.main_fragment)
        NavigationUI.setupActionBarWithNavController(this, navController)
    }

    override fun onSupportNavigateUp(): Boolean {
        val navController = this.findNavController(R.id.main_fragment)
        return navController.navigateUp()
    }

    override fun onStop() {
        super.onStop()

        // Write the dictionary file into the disk.
        this.openFileOutput("dictionary", Context.MODE_PRIVATE).use {
            Dictionary.serialize(it)
        }
    }
}
