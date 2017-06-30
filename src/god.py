#-*- coding: utf-8 -*-

import json
from random import randint

class God:

    numCard = [1,2,3,4,5,6,7,8,9,10,11,12,13] # Numero de la carte
    peer = 0                                  # Pair ou impair
    cardType = ['S', 'D', 'C', 'H']           # Type de la carte
    colorsPlayed = []                         # Couleur jouee
    colorsChecked = 0                         # Nomnbre de couleurs verifiees dans les cartes jouees qui correspondent a la regle
    numberCardsToPut = [1,2,3,4,5]            # Nombre de cartes posees par le joueur
    redundancy = [0,1,2,3,4]                  # Nombre de cartes intermediaires a retrouver entre chaque bonnes cartes imposees par la regle
    alternatingColors = 0                     # Alternance des couleurs ex: une rouge puis une noir etc ...
    alternance = 0                            # Alternance a retrouver dans les cartes a jouer
    totalNum = 0                              # Somme des numeros de cartes qui doit etre superieur a un certain nombre
    numMin = 0                                # Numero de carte minimum a retrouver dans les cartes jouees
    finalCheck = []                           # Liste contenant les resultats de toutes les fonctions afin de savoir si au moins une regle n'a pas ete respectee

    # Fonction qui retourne des cartes de test
    def getCardsTest(self):
        data = json.dumps({'cards':[{'color': 'H','number': 2}, {'color':'C','number':3}, {'color':'C','number':2}]})
        item_dict = json.loads(data)
        for i in item_dict['cards']:
            if i['color'] == 'S':
                i['color'] = 1
            elif i['color'] == 'D':
                i['color'] = 2
            elif i['color'] == 'C':
                i['color'] = 3
            elif i['color'] == 'H':
                i['color'] = 4

        return data

    # Fonction qui retourne un exemple type de regle a des fins de test
    def getFakeRule(self):
        data = {'numberCardsToPut':3,'color':0,'numCard':None,'cardType':randint(1,4),'redundancy':0, 'alternating_colors':0, 'totalNum': 7}
        return data

    # Fontion qui retourne une regle aleatoire
    def getRandomRule(self):
        data = {'numberCardsToPut':randint(1,5),'color':randint(0, 1),'numCard':randint(1,13),'cardType':randint(1,4),'redundancy':randint(0,4), 'alternating_colors':randint(0,1), 'totalNum': randint(1,100)}
        return data

    # ***********************************************************************************************************
    # *    Fonction principale qui fait appel a toutes les fonctions de verification implementees en dessous    *
    # ***********************************************************************************************************
    def checkRules(self):
        cardsPlayed = self.getCardsTest()
        item_dict = json.loads(cardsPlayed)
        #rule = self.getFakeRule()
        rule = self.getRandomRule()
        ruleColor = rule['color']
        nbCardsToPut = rule['numberCardsToPut']
        self.finalCheck.append(self.checkAllColors(item_dict,ruleColor))
        self.finalCheck.append(self.checkNbCards(item_dict,nbCardsToPut))
        self.finalCheck.append(self.checkAltertatingColor(rule,item_dict))
        self.finalCheck.append(self.checkTotalNum(item_dict,rule))

        if False in self.finalCheck:
            return False
        else:
            return True
    # ***********************************************************************************************************
    # *                                                                                                         *
    # ***********************************************************************************************************

    # TODO : Générer une règle random et vérifier si la partie est déjà commencée ou pas pour ne pas générer à chaque tour de joueur une nouvelle règle

    # Fonction qui verifie si toutes les couleurs correspondent a celle imposee par la regle
    def checkAllColors(self,item_dict,ruleColor):
        self.getColorsPlayed(item_dict)
        for j in self.colorsPlayed:
            if j == ruleColor:
                self.colorsChecked += 1
        if len(self.colorsPlayed) == len(item_dict['cards']):
            return True
        else:
            return False

    # Fonciton qui verifie si le joueur a poser le nombre de cartes impose par la regle
    def checkNbCards(self,item_dict,nbCardsToPut):
        if len(item_dict['cards']) == nbCardsToPut:
            return True
        else:
            return False

    # Fonction qui verifie si une alternance de couleurs est presente dans les cartes jouees
    # dans le cas ou la regle l impose
    def checkAltertatingColor(self,rule,item_dict):

        nbAlternance = 0

        if rule['alternating_colors'] == 1:
            self.getColorsPlayed(item_dict)
            for indx,val in enumerate(self.colorsPlayed[1:], start=1):
                if (indx < len(self.colorsPlayed)) and (val != self.colorsPlayed[indx-1]):
                        nbAlternance += 1
            if nbAlternance == len(self.colorsPlayed) -1:
                return True
            else:
                return False
        else:
            return "Pas d'alternance de couleurs défini dans les règles"

    # Fonction qui attribue une liste des couleurs retrouvee dans les cartes jouees dans la variable "colorsPlayed"
    # Rouge = 1, Noir = 0
    def getColorsPlayed(self,item_dict):
        for x in item_dict['cards']:
            if (x['color'] == 2) or (x['color'] == 4):
                self.colorsPlayed.append(1)
            elif (x['color'] == 3) or (x['color'] == 1):
                self.colorsPlayed.append(0)

    # Fonction qui verifie si la somme des numeros de cartes correspond au numero impose par la regle
    def checkTotalNum(self,item_dict,rule):
        for i in item_dict['cards']:
            self.totalNum += i['number']
        if self.totalNum == rule['totalNum']:
            return True
        else:
            return False

    # Fonction qui affiche la règle en français
    def displayRule(self,rule):
        ruleString = "REGLES DU JEU \n"
        for i in rule:
            if i == 'redundancy':
                ruleString += "Redondance de : " + str(rule[i]) + "\n"
            if i == 'color':
                ruleString += "couleurs : " + str(rule[i]) + "\n"
            if i == 'numCard':
                ruleString += "Numéro de carte : " + str(rule[i]) + "\n"
            if i == 'numberCardsToPut':
                ruleString += "Nombre de cartes à poser : " + str(rule[i]) + "\n"
            if i == 'cardType':
                if rule[i] == 1:
                    ruleString += "Type de cartes : Pic \n"
                if rule[i] == 2:
                    ruleString += "Type de cartes : Carreau \n"
                if rule[i] == 3:
                    ruleString += "Type de cartes : Trèfle \n"
                if rule[i] == 4:
                    ruleString += "Type de cartes : Coeur \n"
            if i == 'alternating_colors':
                if rule[i] == 1:
                    ruleString += "Alternance des couleurs : Oui \n"
                elif rule[i] == 0:
                    ruleString += "Alternance des couleurs : Non \n"
            if i == 'totalNum':
                if rule[i] != None:
                    ruleString += "Somme totale des numéros de cartes : " + str(rule[i]) + " \n"

        return ruleString

    # Fonction qui verifie si un joueur est prophete ou non
    # Dans le cas où dans le deck du joueur en question aucune carte n'est bonne alors il est prophete (True)
    # sinon il ne l'est pas (False)
    def checkIfProphet(self):
        checkedDeck = self.checkRules()
        if checkedDeck == False:
            return True
        else:
            return False

if __name__ == '__main__':
    m = God()
    m.displayRule(m.getRandomRule())
    m.checkRules()