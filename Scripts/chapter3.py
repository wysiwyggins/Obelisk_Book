import random
import potions
import chapterQuote
import io

def getAdjective():
    adjectiveFO = io.open("words/adjectives.txt", encoding="utf-8")
    adjectiveList = list(adjectiveFO)
    selection = random.randint(0, len(adjectiveList) - 1)
    adjective = adjectiveList[selection]
    adjective = adjective.rstrip("\n")
    return adjective

with open("../Codex/_project/_markdown/Potions.md", "w") as myfile:
    myfile.write("---\ntitle: Potions\ntype: bodymatter\n---\n")
    myfile.write("\n::: chapter:potions\n")
    myfile.write("# Potions\n\n")
    myfile.write(chapterQuote.generateQuote())
    for x in range(40):
        myfile.write("\n\n::: section:potiontable-"+str(x)+" classes:\"break-after\"\n")
        #adjective = getAdjective()
        #myfile.write("\n*" + adjective.capitalize() + " Potions-*\n")
        myfile.write("| Reagent 1 | Reagent 2 | Reagent 3 | Appearance | Effect |\n")
        myfile.write("|-|-|-|-|-|\n")
        for y in range(15):
            newPotion = potions.Potion()
            newPotion.generatePotion()
            myfile.write(str(newPotion))
        myfile.write("\n\n::: exit:potiontable-"+str(x)+"\n\n")
    myfile.write("\n\n::: exit:potions\n")