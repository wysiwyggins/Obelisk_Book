import random
import io
import os
import string

#this is the rune picker! Be sure you've run the obelisk_glyphs jupyter notebook first to make a bunch of svg glyphs in the Codex/_project/_images/glyphs folder!
class Rune:
    
    def makeDictionary():
        files = os.listdir("../Codex/_project/_images/glyphs/")
        runeDict = { }
        for glyph in files:
            meaning = (random.choice(open("corpus/fantasy.txt").read().split()))
            meaning = meaning.replace('.', '').replace(',', '')
            runeDict[meaning] = glyph
        print(runeDict)
    

Rune.makeDictionary()

# print(Rune.meaning)