import random
import runes
import chapterQuote
import io

def getAdjective():
    adjectiveFO = io.open("words/adjectives.txt", encoding="utf-8")
    adjectiveList = list(adjectiveFO)
    selection = random.randint(0, len(adjectiveList) - 1)
    adjective = adjectiveList[selection]
    adjective = adjective.rstrip("\n")
    return adjective

with open("../Codex/_project/_markdown/Runes.md", "w") as myfile:
    myfile.write("---\ntitle: Runes\ntype: bodymatter\n---\n")
    myfile.write("\n::: chapter:chapter-five\n")
    myfile.write("\n::: section:page classes:\"break-after\"\n")
    myfile.write("# Runes\n\n")
    myfile.write(chapterQuote.generateQuote())
    myfile.write("\n::: exit:page\n")

    runes = runes.Runes()
    runeCounter= 0
    myfile.write("\n::: section:runetable-1 classes:\"break-after\"\n")
    myfile.write("| Glyph | Translation |\n")
    myfile.write("|-|-|\n")
    for rune in runes.runeDict:
        runeCounter += 1
        myfile.write('|<img src=\"../images/glyphs/'+runes.runeDict[rune]+'\" ' + 'alt=\"A glyph made from wedge-shaped marks\"/> |' + rune + ' |\n')
        if runeCounter % 10 == 0:
            nextSectionNumber = str(runeCounter *.1)
            lastSectionNumber = str(runeCounter *.1-1)
            myfile.write("\n::: exit:runetable-"+ lastSectionNumber + "\n\n")
            myfile.write("\n::: section:runetable-"+ nextSectionNumber +" classes:\"break-after\"\n")
            myfile.write("| Glyph | Translation |\n")
            myfile.write("|-|-|\n")
        if runeCounter >= len(runes.runeDict) and runeCounter % 10 != 0:
            print("I think I'm done")
            myfile.write("\n::: exit:runetable-"+ lastSectionNumber + "\n\n")




    myfile.write("::: exit:chapter-five\n")

    #| ::: figure:glyph-'+str(runeCounter) +' source:' + runes.runeDict[rune]