import random
import io


class Wand:
    def __init__(self):
        self.r1 = "?"
        self.r2 = "?"
        self.r3 = "?"
        self.name = "Molybednum Wand"
        self.effect = "Wand of Strength"

    def getSkill(self):
        skillFO = io.open("words/skills.txt", encoding="utf-8")
        skillList = list(skillFO)
        selection = random.randint(0, len(skillList) - 1)
        skill = skillList[selection]
        skill = skill.rstrip("\n")
        return skill

    def getAdjective(self, reversed):
        adjectiveFO = io.open("words/adjectives.txt", encoding="utf-8")
        adjectiveList = list(adjectiveFO)
        selection = random.randint(0, len(adjectiveList) - 1)
        # This lets us pick from two different random names with the same seed, for two adjectives in one character.
        if reversed == True:
            adjective = adjectiveList[-selection]
        else:
            adjective = adjectiveList[selection]
        adjective = adjective.rstrip("\n")
        return adjective

    def getSubstance(self):
        substanceFO = io.open("words/substances.txt", encoding="utf-8")
        substanceList = list(substanceFO)
        selection = random.randint(0, len(substanceList) - 1)
        substance = substanceList[selection]
        substance = substance.rstrip("\n")
        return substance

    def generateWand(self):
        adjective = self.getAdjective(False)
        substance = self.getSubstance()
        skill = self.getSkill()
        self.name = substance.capitalize() + " Wand"
        wandEffectChance = random.randint(0,2)
        if wandEffectChance == 0:
            self.effect = adjective.capitalize() + " Wand"
        else:
            self.effect = "Wand of " + skill.capitalize()
        # masking some cells
        substanceOrEffect = random.randint(0,1)
        if substanceOrEffect == 0:
            self.name = "???"
        else:
            self.effect = "???"

    def __str__(self):
        return ' | ' + self.name + ' | ' + self.effect +' |\n'
