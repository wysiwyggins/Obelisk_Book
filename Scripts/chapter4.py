import random
import runes
import chapterQuote
import io

with open("../Codex/_project/_markdown/Runes.md", "w") as myfile:
    myfile.write("---\ntitle: Runes\ntype: bodymatter\n---\n")
    myfile.write("\n::: chapter:runes\n")
    myfile.write("# Runes\n\n")
    myfile.write(chapterQuote.generateQuote())

    runes = runes.Runes()
    runeCounter= 0
    myfile.write("\n\n\n")
    myfile.write("| Glyph | Translation |\n")
    myfile.write("|-|-|\n")
    for rune in sorted(runes.runeDict):
        runeCounter += 1
        myfile.write('|<img src=\"../images/glyphs/'+runes.runeDict[rune]+'\" ' + 'alt=\"A glyph made from wedge-shaped marks\"/> |' + rune + ' |\n')
        if runeCounter % 12 == 0:
            nextSectionNumber = str(int(runeCounter *.1))
            lastSectionNumber = str(int(runeCounter *.1-1))
            myfile.write("\n\n")
            myfile.write("| Glyph | Translation |\n")
            myfile.write("|-|-|\n")
        if runeCounter >= len(runes.runeDict) and runeCounter % 12 != 0:
            print("I think I'm done")



    myfile.write("\n\n::: exit:runes\n")

    #| ::: figure:glyph-'+str(runeCounter) +' source:' + runes.runeDict[rune]