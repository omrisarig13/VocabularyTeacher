package com.vocabularyteacher.vocabularyteacher

enum class KnowledgeLevels(var knowledgeLevel: Int) {
    UNKNOWN(0),
    INEXPERIENCE(1),
    MEDIUM(2),
    EXPERIENCED(3),
    KNOWN(4);

    operator fun inc(): KnowledgeLevels {
        // TODO: Understand how to do it nicer.
        return when (this.knowledgeLevel) {
            UNKNOWN.knowledgeLevel -> INEXPERIENCE
            INEXPERIENCE.knowledgeLevel -> MEDIUM
            MEDIUM.knowledgeLevel -> EXPERIENCED
            else -> KNOWN
        }
    }

    operator fun dec(): KnowledgeLevels {
        // TODO: Understand how to do it nicer.
        return when (this.knowledgeLevel) {
            KNOWN.knowledgeLevel -> EXPERIENCED
            EXPERIENCED.knowledgeLevel -> MEDIUM
            MEDIUM.knowledgeLevel -> INEXPERIENCE
            else -> UNKNOWN
        }
    }

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