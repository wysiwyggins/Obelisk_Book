import random
import instructions
import chapterQuote
import io
import os
import markovify
import spacy
from unidecode import unidecode



def generateInstructions():
    files = os.listdir("../Codex/_project/_images/instructions/")
    nonHiddenFiles = [ filename for filename in files  if not filename.startswith(".") ]
    instructionsNumber = random.randint(0, len(nonHiddenFiles)-1)
    instructionsImage = nonHiddenFiles[instructionsNumber]
    instructionText = " "

    nlp = spacy.load("en_core_web_sm")
    with open("corpus/instructions.txt") as f:
        text = f.read()

    text_model = markovify.Text(text)
    text_model = text_model.compile()

    class POSifiedText(markovify.Text):
        def word_split(self, sentence):
            return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

        def word_join(self, words):
            sentence = " ".join(word.split("::")[0] for word in words)
            return sentence

    print("generating...")
    instructionText += '\n<img src=\"../images/instructions/'+instructionsImage+'\" ' + 'alt=\"An interface graphic\"/>\n'
    for number in range(10):
        try: 
            instructionText += "\n" + text_model.make_short_sentence(250) + " "
        except:
            instructionText = text_model.make_sentence()
    
    return instructionText


with open("../Codex/_project/_markdown/Instructions.md", "w") as myfile:
    myfile.write("---\ntitle: Instructions\ntype: bodymatter\n---\n")
    myfile.write("\n::: chapter:instructions\n")
    myfile.write("# instructions\n\n")
    myfile.write("\n::: figure-inline:figure-one source:interface.png alt:\"Image of Obelisk game interface\"\n:: 1. Game Year and Zodiac, Character Name  2. Moon Phase, Soul Tokens  3. Action Cursor    4. Player Character     5. Verb Palette\n::")
    myfile.write("\n\nTo play Obelisk, use the mouse to click on an area to guide your character to it. To carry out an action, right click to cycle actions, or click an action button, then click on an area where you would like to carry out that action.")
    myfile.write("\n\n::: figure-inline:mouse source:mouse.jpg alt:\"A Macintosh mouse control device\"\n\n")
    for x in range(10):
        newinstruction = generateInstructions()
        myfile.write("\n\n")
        myfile.write(str(newinstruction))
        myfile.write("\n\n")
    myfile.write("\n\n::: exit:instructions\n\n")
