package com.example.vocabularyteacher

enum class KnowledgeLevels(val knowledgeLevel: Int) {
    UNKNOWN(0),
    INEXPERIENCE(1),
    MEDIUM(2),
    EXPERIENCED(3),
    KNOWN(4);

    companion object {
        fun from(findValue: Int): KnowledgeLevels? {
            for (value in KnowledgeLevels.values()) {
                if (value.knowledgeLevel == findValue) {
                    return value
                }
            }
            return null
        }
    }
}