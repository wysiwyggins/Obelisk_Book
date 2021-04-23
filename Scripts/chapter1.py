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
    myfile.write("\n::: chapter:chapter-one\n")
    myfile.write("\n::: section:page classes:\"break-after\"\n")
    myfile.write("# Introduction\n\n")
    myfile.write("\n::: blockquote:introduction:\n")
    myfile.write("No matter how elaborate Cluthos' evasions, he failed to disarm the traps that had been laid for him. The walls of his prison still stood firm, no matter how vast the continent within their borders grew. Each new spell that Cluthos wove was longer and more convoluted than the last– until it took weeks for his parched lips to speak them, and the syllables dissolved into inchoate sounds. *There must have been a time before or after captivity*, but Cluthos could imagine neither, and his dreams of freedom always crowned him king of nowhere, under the inescapable shadow of yet another looming obelisk.")
    myfile.write("\n::: exit:introduction\n")
    myfile.write("*–The Book of Secrets*")
    myfile.write("\n::: exit:page\n")

    myfile.write("## Welcome to the incredible world of *Obelisk*!\n\n")
    myfile.write("In obelisk you play the role of an adventurer on a quest for one of many legendary *capstones of power*. You (or you and your friends, via the new ObeliskNet service[^1] ) will explore vast lands and interact with a varied cast of characters as you seek magical supremacy.) \n\nThis book serves as your guide through the many mysteries of the world of Obelisks!\n")

    myfile.write("[^1]: ObeliskNet requires a local AppleTalk connection or modem and corresponding ObeliskNet server software\n")
    myfile.write("::: exit:chapter-one\n")
