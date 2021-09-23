import random
import realms
import chapterQuote
import io



with open("../Codex/_project/_markdown/Realms.md", "w") as myfile:
    myfile.write("---\ntitle: Realms\ntype: bodymatter\n---\n")
    myfile.write("\n::: chapter:realms\n")
    myfile.write("# Realms\n\n")
    myfile.write(chapterQuote.generateQuote())
    
    for x in range(10):
        newRealm = realms.generateRealm()
        myfile.write("\n\n")
        myfile.write("\n\n::: section:realm-"+str(x)+" classes:\"break-after\"\n")
        myfile.write(str(newRealm))
        myfile.write("\n\n")
        myfile.write("\n::: exit:realm-"+str(x)+"\n\n")
    myfile.write("\n\n::: exit:realms\n\n")

    #| ::: figure:glyph-'+str(runeCounter) +' source:' + runes.runeDict[rune]