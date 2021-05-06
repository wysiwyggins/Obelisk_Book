import io
import random
import re
import os

import markovify
import spacy
from hashids import Hashids
from unidecode import unidecode

def addAorAn(word):
        if word[-1] != "s" and word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
            word = "an " + word
        elif word[-1] != "s":
            word = "a " + word
        return word

def getSubstance():
        substanceFO = io.open("words/substances.txt", encoding="utf-8")
        substanceList = list(substanceFO)
        selection = random.randint(0, len(substanceList) - 1)
        substance = substanceList[selection]
        substance = substance.rstrip("\n")
        return substance

def getReagent():
    reagentsFO = io.open("words/reagents.txt", encoding="utf-8")
    reagentsList = list(reagentsFO)
    selection = random.randint(0, len(reagentsList) - 1)
    reagent = reagentsList[selection]
    while "#" in reagent:
        selection = random.randint(0, len(reagentsList) - 1)
        reagent = reagentsList[selection]
    reagent = reagent.rstrip("\n")
    return reagent

def getAdjective():
    adjectiveFO = io.open("words/adjectives.txt", encoding="utf-8")
    adjectiveList = list(adjectiveFO)
    selection = random.randint(0, len(adjectiveList) - 1)
    adjective = adjectiveList[selection]
    adjective = adjective.rstrip("\n")
    return adjective


def generateRealm():
    files = os.listdir("../Codex/_project/_images/maps/")
    mapNumber = random.randint(0, len(files)-1)
    mapImage = files[mapNumber]
    hashids = Hashids()
    title = " "
    realmText = " "

    nlp = spacy.load("en_core_web_sm")
    with open("corpus/fantasy.txt") as f:
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

    title= "A Forgotten Place"
    hashids = Hashids(salt=title)
    id = hashids.encode(1, 2, 3)
    adjective = getAdjective()
    realmText += '\n<img src=\"../images/maps/'+mapImage+'\" ' + 'alt=\"A map of a forgotten place\"/>\n'
    realmText += "\n## "+ title.title()+"\n\n"
    realmText += ""
    realmText += "This was once known to be " +  addAorAn(adjective) + " land. Exports included " + getReagent() + ", " + getSubstance() + ", " + getSubstance() +" and " + getReagent() +". It was conquored and forgotten.\n"
    for number in range(20):
        try: 
            realmText += "\n" + text_model.make_short_sentence(250) + " "
        except:
            realmText = text_model.make_sentence()
    
    return realmText
