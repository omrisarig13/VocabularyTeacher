package com.vocabularyteacher.vocabularyteacher

import java.io.FileInputStream
import java.io.FileOutputStream

object Dictionary {
    val wordList = mutableListOf<WordCouple>()

    fun addWordCouple(newWordCouple: WordCouple): Boolean {
        for (wordCouple in this.wordList) {
            if (wordCouple == newWordCouple) {
                return false
            }
        }
        this.wordList.add(newWordCouple)
        return true
    }

    fun clearDictionary() {
        this.wordList.clear()
    }

    fun serialize(openedFile: FileOutputStream) {
        for (wordCouple in this.wordList) {
            openedFile.write(wordCouple.toByteArray())
        }
    }

    fun loadSerialized(serializedFile: FileInputStream?) {
        if (serializedFile == null) {
            return
        }

        var newWord: WordCouple? = createSerializedWordCouple(serializedFile)
        while (newWord != null) {
            this.addWordCouple(newWord)
            newWord = createSerializedWordCouple(serializedFile)
        }
    }

    fun getRandomOrderedWordsFromLevel(wantedKnowledgeLevel: KnowledgeLevels): MutableList<WordCouple> {
        val internalWordList = this.wordList.filter { it.knownLevel == wantedKnowledgeLevel }
        val mutableWordList = internalWordList.toMutableList()
        mutableWordList.shuffle()
        return mutableWordList
    }

}
