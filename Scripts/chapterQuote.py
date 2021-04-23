import io
import random
import re

import markovify
import spacy
from hashids import Hashids
from unidecode import unidecode


def generateQuote():
    hashids = Hashids()
    title = " "
    quoteText = " "
    index = 0
    codexList = []

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

    try:
        title = text_model.make_short_sentence(50)
        title = title[:-1]
    except:
        title = text_model.make_short_sentence(100)
    hashids = Hashids(salt=title)
    quoteText += "\n::: blockquote:book_of_secrets:\n"
    for number in range(3):
        try: 
            quoteText += "\n" + text_model.make_short_sentence(100) + " "
        except:
            quoteText = text_model.make_short_sentence(200)
    quoteText += "\n::: exit:book_of_secrets\n"
    quoteText += "*–"+ title.title()+"*"
    
    return quoteText

def generateTitle():
    hashids = Hashids()
    title = " "
    quoteText = " "
    index = 0
    codexList = []

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

    try:
        title = text_model.make_short_sentence(50)
        title = title[:-1]
    except:
        title = text_model.make_short_sentence(100)
    title = "*–"+ title.title()+"*"
    return title


#print(generateQuote())