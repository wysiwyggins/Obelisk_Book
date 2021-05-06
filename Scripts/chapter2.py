import random
import realms
import chapterQuote
import io



with open("../Codex/_project/_markdown/Realms.md", "w") as myfile:
    myfile.write("---\ntitle: Realms\ntype: bodymatter\n---\n")
    myfile.write("\n::: chapter:chapter-two\n")
    myfile.write("# Realms\n\n")
    myfile.write(chapterQuote.generateQuote())
    
    for x in range(10):
        newRealm = realms.generateRealm()
        myfile.write("\n\n")
        myfile.write(str(newRealm))
        myfile.write("\n\n")
    myfile.write("\n\n::: exit:chapter-two\n\n")

    #| ::: figure:glyph-'+str(runeCounter) +' source:' + runes.runeDict[rune]