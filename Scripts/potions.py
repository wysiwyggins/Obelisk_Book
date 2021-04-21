import random
import io


class Potion:
    def __init__(self):
        self.r1 = "?"
        self.r2 = "?"
        self.r3 = "?"
        self.name = "Swirly Potion"
        self.effect = "Potion of Strength"

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

    def getColor(self):
        colorFO = io.open("words/colors.txt", encoding="utf-8")
        colorList = list(colorFO)
        selection = random.randint(0, len(colorList) - 1)
        color = colorList[selection]
        color = color.rstrip("\n")
        return color

    def getReagent(self):
        reagentsFO = io.open("words/reagents.txt", encoding="utf-8")
        reagentsList = list(reagentsFO)
        selection = random.randint(0, len(reagentsList) - 1)
        reagent = reagentsList[selection]
        while "#" in reagent:
            selection = random.randint(0, len(reagentsList) - 1)
            reagent = reagentsList[selection]
        reagent = reagent.rstrip("\n")
        return reagent

    def generatePotion(self):
        adjective = self.getAdjective(False)
        color = self.getColor()
        skill = self.getSkill()
        reagent1 = self.getReagent()
        reagent2 = self.getReagent()
        reagent3 = self.getReagent()
        self.r1 = reagent1
        self.r2 = reagent2
        self.r3 = reagent3
        self.name = color.capitalize() + " Potion"
        reagentEffectChance = random.randint(0,2)
        if reagentEffectChance == 0:
            self.effect = adjective.capitalize() + " Potion"
        else:
            self.effect = "Potion of " + skill.capitalize()
        # masking some cells
        colorOrEffect = random.randint(0,1)
        if colorOrEffect == 0:
            self.name = "???"
        else:
            self.effect = "???"
        missingReagents = random.randint(0,3)
        if missingReagents == 1:
            cell = random.randint(1,3)
            if cell == 1:
                self.r1 = "???"
            if cell == 2:
                self.r2 = "???"
            if cell == 3:
                self.r3 = "???"
        if missingReagents == 2:
            cells = random.randint(1,3)
            if cells == 1:
                self.r1 = "???"
                self.r2 = "???"
            if cells == 2:
                self.r2 = "???"
                self.r3 = "???"
            if cells == 3:
                self.r1 = "???"
                self.r3 = "???"

    def __str__(self):
        return ' | ' + self.r1 + ' | ' + self.r2 + ' | ' + self.r3 + ' | ' + self.name + ' | ' + self.effect +' |\n'

#newPotion = Potion()
#newPotion.generatePotion()
#print(newPotion)
