import random
import io
import os
import string
import enchant



#this is the rune picker! Be sure you've run the obelisk_glyphs jupyter notebook first to make a bunch of svg glyphs in the Codex/_project/_images/glyphs folder!
class Runes:
    
    def __init__(self):
        d = enchant.Dict("en_US")
        files = os.listdir("../Codex/_project/_images/glyphs/")
        self.runeDict = { }
        for glyph in files:
            if not glyph.startswith('.'):
                meaning = (random.choice(open("corpus/fantasy.txt").read().split()))
                while meaning in self.runeDict or len(meaning) < 4 or "–" in meaning:
                    meaning = (random.choice(open("corpus/fantasy.txt").read().split()))
                meaning = meaning.replace('.', '').replace(',', '').replace(';', '').replace(':', '').replace('“', '').replace('"', '').replace('”', '').replace('!', '').replace('\'', '').lower()
                if d.check(meaning):
                    meaning = meaning.lower()
                    #print(meaning + " is a word I already know.")
                else:
                    if "less" in meaning or meaning.endswith("s") or "-" in meaning or "like" in meaning:
                        meaning = meaning.lower()
                    else:
                        #print("I guess " + meaning + " is a proper noun.")
                        meaning = meaning.capitalize()
                self.runeDict[meaning] = glyph
        #print(self.runeDict)

    

