import random
import potions
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
    myfile.write("\n::: chapter:chapter-four\n")
    myfile.write("# Potions\n\n")
    for x in range(50):
        #adjective = getAdjective()
        #myfile.write("## " + adjective.capitalize() + " Potions-\n")
        myfile.write("\n\n")
        myfile.write("| Reagent 1 | Reagent 2 | Reagent 3 | Appearance | Effect |\n")
        myfile.write("|-|-|-|-|-|\n")
        for y in range(14):
            newPotion = potions.Potion()
            newPotion.generatePotion()
            myfile.write(str(newPotion))
    myfile.write("::: exit:chapter-four\n")