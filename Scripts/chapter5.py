import random
import wands
import chapterQuote
import io

def getAdjective():
    adjectiveFO = io.open("words/adjectives.txt", encoding="utf-8")
    adjectiveList = list(adjectiveFO)
    selection = random.randint(0, len(adjectiveList) - 1)
    adjective = adjectiveList[selection]
    adjective = adjective.rstrip("\n")
    return adjective

with open("../Codex/_project/_markdown/Wands.md", "w") as myfile:
    myfile.write("---\ntitle: Wands\ntype: bodymatter\n---\n")
    myfile.write("\n::: chapter:wands\n")
    myfile.write("# Wands\n\n")
    myfile.write(chapterQuote.generateQuote())
    for x in range(40):
        myfile.write("\n\n::: section:wandtable-"+str(x)+" classes:\"break-after\"\n")
        adjective = getAdjective()
        myfile.write("\n*" + adjective.capitalize() + " wands-*\n")
        myfile.write("| Material | Effect |\n")
        myfile.write("|-|-|\n")
        for y in range(10):
            newWand = wands.Wand()
            newWand.generateWand()
            myfile.write(str(newWand))
        myfile.write("\n::: exit:wandtable-"+str(x)+"\n\n")
    myfile.write("::: exit:wands\n")