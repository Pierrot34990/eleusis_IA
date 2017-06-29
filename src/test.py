import json

class Main:

    numCard = [1,2,3,4,5,6,7,8,9,10,11,12,13] # Numero de la carte
    peer = ['yes','no']                       # Pair ou impair
    cardType = ['S', 'D', 'C', 'H']           # Type de la carte
    colorPlayed = []                          # Couleur jouee
    colorsChecked = 0                         # Nomnbre de couleurs verifiees qui correspondent a la regle
    numberCardsToPut = [1,2,3,4,5]            # Nombre de cartes posees par le joueur
    redundancy = [0,1,2,3,4]                  # Nombre de cartes intermediaires a retrouver entre chaque bonnes cartes impose par la regle
    alternatingColors = ['yes', 'no']         # Alternance des couleurs ex: une rouge puis une noir etc ...
    # TODO : Somme des numeros de cartes qui doit etre superieur a un certain nombre

    # Fonction qui retourne des cartes de test
    def getCardsTest(self):
        data = json.dumps({'cards':[{'color': 'S','number': 2}, {'color':'C','number':3}]})
        return data

    # Fonction qui retourne un exemple type de regle a des fins de test
    def getFakeRule(self):
        data = {'numberCardsToPut':2,'color':'noir','numCard':None,'cardType':None,'redundancy':0, 'alternating_color':'no'}
        return data

    # Fonction principale qui fait appel a toutes les fonctions de verification implementees en dessous
    def checkRules(self):
        cardsPlayed = self.getCardsTest()
        item_dict = json.loads(cardsPlayed)
        rule = self.getFakeRule()
        ruleColor = rule['color']
        nbCardsToPut = rule['numberCardsToPut']
        print self.checkAllColors(item_dict,ruleColor)
        print self.checkNbCards(item_dict,nbCardsToPut)
        print self.checkAltertatingColor(self,rule)


    # Fonction qui verifie si toutes les couleurs correspondent a celle imposee par la regle
    def checkAllColors(self,item_dict,ruleColor):
        for i in item_dict['cards']:
            if (i['color'] == 'D') or (i['color'] == 'H'):
                self.colorPlayed.append('rouge')
            elif(i['color'] == 'C') or (i['color'] == 'S'):
                self.colorPlayed.append('noir')
                for j in self.colorPlayed:
                    if j == ruleColor:
                        self.colorsChecked += 1
        if len(self.colorPlayed) == len(item_dict['cards']):
            return "Bonne couleurs"
        else:
            return "Mauvaises couleurs"

    # Fonciton qui verifie si le joueur a poser le nombre de cartes impose par la regle
    def checkNbCards(self,item_dict,nbCardsToPut):
        if len(item_dict['cards']) == nbCardsToPut:
            return "Bon nb de cartes"
        else:
            return "Mauvais nombre de cartes"

    # Fonction qui verifie si une alternance de couleurs est presente dans les cartes jouees
    # dans le cas ou la regle l impose
    def checkAltertatingColor(self,rule):
        if rule['alternating_color'] == 'yes':

        else:
            return "Pas d'alternance de couleurs défini dans les règles"

if __name__ == '__main__':
    m = Main()
    m.checkRules()