import random
import io
import os
import string

#this is the rune picker! Be sure you've run the obelisk_glyphs jupyter notebook first to make a bunch of svg glyphs in the Codex/_project/_images/glyphs folder!
class Runes:
    
    def __init__(self):
        files = os.listdir("../Codex/_project/_images/glyphs/")
        self.runeDict = { }
        for glyph in files:
            meaning = (random.choice(open("corpus/fantasy.txt").read().split()))
            while meaning in self.runeDict or len(meaning) < 4:
                meaning = (random.choice(open("corpus/fantasy.txt").read().split()))
            meaning = meaning.replace('.', '').replace(',', '').replace(';', '').replace(':', '')
            self.runeDict[meaning] = glyph
        #print(self.runeDict)

    

