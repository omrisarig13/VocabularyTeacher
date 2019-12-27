package com.vocabularyteacher.vocabularyteacher

import java.io.FileInputStream

data class WordCouple(
    var nativeWord: String,
    var translatedWord: String,
    var knownLevel: KnowledgeLevels = KnowledgeLevels.UNKNOWN,
    val questionInLevel: Int = 3
) {
    private var correctAnswersInLevel = 0

    override fun toString(): String {
        return "${this.nativeWord} : ${this.translatedWord} [${this.knownLevel}]"
    }

    fun toByteArray(): ByteArray {
        var serializedValue = ByteArray(0)

        val nativeWordByteArray = nativeWord.toByteArray()
        val translatedWordByteArray = translatedWord.toByteArray()

        serializedValue += nativeWordByteArray.size.toByte()
        serializedValue += nativeWord.toByteArray()
        serializedValue += translatedWordByteArray.size.toByte()
        serializedValue += translatedWord.toByteArray()
        serializedValue += knownLevel.knowledgeLevel.toByte()
        return serializedValue
    }

    override fun equals(other: Any?): Boolean {
        if (other is WordCouple) {
            return other.nativeWord == this.nativeWord && other.translatedWord == this.translatedWord
        }
        return false
    }

    fun userAnsweredCorrectly() {
        if (this.knownLevel < KnowledgeLevels.KNOWN) {
            this.correctAnswersInLevel++
            if (this.correctAnswersInLevel >= this.questionInLevel) {
                this.correctAnswersInLevel = 0
                this.knownLevel++
            }
        }
    }

    fun userAnsweredWrong() {
        if (this.knownLevel > KnowledgeLevels.UNKNOWN) {
            this.correctAnswersInLevel--
            if (this.correctAnswersInLevel <= -this.questionInLevel) {
                this.correctAnswersInLevel = 0
                this.knownLevel--
            }
        }
    }
}

fun createSerializedWordCouple(serializedFile: FileInputStream): WordCouple? {
    // Read the native word from the byte array
    val nativeWordLength = ByteArray(1)
    if (1 != serializedFile.read(nativeWordLength)) {
        return null
    }
    val nativeWordByteArray = ByteArray(nativeWordLength[0].toInt())
    if (nativeWordByteArray.size != serializedFile.read(nativeWordByteArray)) {
        return null
    }
    val nativeWord = String(nativeWordByteArray)

    // Read the translated word from the byte array
    val translatedWordLength = ByteArray(1)
    if (1 != serializedFile.read(translatedWordLength)) {
        return null
    }
    val translatedWordByteArray = ByteArray(translatedWordLength[0].toInt())
    if (translatedWordByteArray.size != serializedFile.read(translatedWordByteArray)) {
        return null
    }
    val translatedWord = String(translatedWordByteArray)

    // Read the knowledge level from the file
    val knowledgeLevelByteArray = ByteArray(1)
    if (1 != serializedFile.read(knowledgeLevelByteArray)) {
        return null
    }
    val knowledgeLevel = KnowledgeLevels.from(knowledgeLevelByteArray[0].toInt()) ?: return null

    return WordCouple(nativeWord, translatedWord, knowledgeLevel)
}
