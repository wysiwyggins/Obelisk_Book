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

with open("../Codex/_project/_markdown/Introduction.md", "w") as myfile:
    myfile.write("---\ntitle: Introduction\ntype: bodymatter\n---\n")
    myfile.write("\n\n::: chapter:chapter-one\n")
    myfile.write("# Introduction\n\n")
    myfile.write("\n\n::: blockquote:ch1quote citation:\"Unknown Author, *The Book of Secrets*\" classes:\"break-after\"")
    myfile.write("\n\nI used to think I had bought my freedom on that day, but in truth, I had taken up residence inside my own dreams- while the world was crumbling around us. As vast, elaborate and real as those dreams seemed, they were only shadows of the prison I had helped build.")
    myfile.write("\n\n::: exit:ch1quote\n")

    myfile.write("## Welcome to the incredible world of Obelisk!\n\n")
    myfile.write("In obelisk you play the role of an adventurer on a quest for one of many legendary *capstones of power*. You (or you and your friends, via the new ObeliskNet service[^1] ) will explore vast lands and interact with a varied cast of characters as you seek magical supremacy.)\n\nThis book serves as your guide through the many mysteries of the world of Obelisks!\n\n\n\n")
    myfile.write("## What is an Obelisk? ##\n\n")
    myfile.write("In a primeval land, tribal peoples once sought great stones to give as dowry. These stones were used to build a new families' home on earth. Stones were also an offering to the dead, building their fortresses in the afterlife, protecting them from demons. These stones formed a sort of ceremonial currency, and the quarrymasters became powerful as stone dwindled and need grew.  Some people became deeply indebted to quarrymasters, enough to enter servitude to them as pawns, or to give their family members over to them to work cutting stone, ever deeper. Some tribes, desperate to free themselves or loved ones, began to take ???loans??? of stone from the funerary obelisks of their ancestors, transferring their debts to the dead. \n Adventurer! you were born into a time of great upheaval and potential! The dead demand tribute, and promise treasure and glory to those who obey.\n\n")

    myfile.write("[^1]: ObeliskNet requires a local AppleTalk connection or modem and corresponding ObeliskNet server software\n")
    myfile.write("::: exit:chapter-one\n")
